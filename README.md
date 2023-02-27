# LiveCommentaryPrediction

This is the beginning of my masters project


 ### Order to run scripts

 First fill in the video file names, the times for games and the goal.com page for the match into match_event_data.csv

 Run Entity Scraper to scrape the team/player names and match details

 Run VideoEditor to stitch and trim the videos and save the audiofiles

 Run SoundAnalysis to use fb denoiser and seperate commentary and the background crowd noise

 Run Transciber to use OpenAIs Whisper to transcribe the commentary

 Run TextProcessing to build datasets from the commentary