use std::collections::HashMap;
use std::process::{Command, Child};
use std::{str, thread, time};

fn main() {
    let mut recordings = HashMap::<String, Child>::new();
    let interval = time::Duration::from_millis(250);
    let mut file_num:u32 = 0;

    loop {
        match run_pactl_command() {
            Ok(output) => {
                let output_str = str::from_utf8(&output.stdout).unwrap();
                let mut current_sources = HashMap::new();

                for line in output_str.lines() {
                    //println!("{}", line);
                    let parts: Vec<&str> = line.split('\t').collect();
                    let source_name = parts[1].to_string();
                    //if source_name.ends_with(".monitor") {
                        //source_name.truncate(source_name.len() - ".monitor".len());
                    //}
                    let running = parts[4] == "RUNNING";
                    current_sources.insert(source_name, running);
                }

                // Determine actions for each source based on the current status
                for (source_name, running) in current_sources {
                    if running && !recordings.contains_key(&source_name) {
                        // Start recording
                        println!("Start recording: {}", source_name);
                        if let Ok(child) = start_recording(&source_name, file_num) {
                            recordings.insert(source_name, child);
                            file_num += 1;
                        }
                    } else if !running && recordings.contains_key(&source_name) {
                        // Stop recording
                        println!("Stop recording: {}", source_name);
                        if let Some(mut child) = recordings.remove(&source_name) {
                            let _ = child.kill();
                        }
                    }
                }
            }
            Err(e) => eprintln!("Failed to execute 'pactl list short sources': {}", e),
        }

        thread::sleep(interval);
    }
}

fn run_pactl_command() -> Result<std::process::Output, std::io::Error> {
    Command::new("pactl")
        .arg("list")
        .arg("short")
        .arg("sources")
        .output()
}

fn start_recording(source_name: &str, file_num: u32) -> Result<Child, std::io::Error> {
    let file_name = format!("WAV/audio_{}.wav", file_num);
    Command::new("pw-record")
        .arg("--target")
        .arg(source_name)
        .arg(file_name) 
        .arg("-P")
        .arg("stream.capture.sink=true")
        .spawn()
}