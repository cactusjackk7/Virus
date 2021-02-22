this is a simple tool to utilize the basic functionality of the Private API From Virus Total, with this tool you can eaisly scan a hash or file (script will automatically hash the file and submit the HASH to VT not the file). You can download malware based on hash, download pcaps, write the full VT Json report to file, and force a rescan of a previously uploaded file with new AV definitions. Advanced queries and bulk downloads can be accomplished via VT Provided Scripts available on the Intelligence portal. (or a bash loop if you want to bulk DL with this)

NOTE: You need your own premium VT API to use this tool. API Key Goes on Line 13!

NOTE2: If you have a free VT Public API (you do) then you can use VTlite.py with limited functionality (Check Hash/Path/Rescan/DownloadJson/VerboseDetections) four checks per minute are allowed.
