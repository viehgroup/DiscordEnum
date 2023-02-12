<H1>Subdomain & Directory Enumeration Tool with Discord Notifications</H1>
A tool for performing subdomain and directory enumeration and receiving notifications of any discovered severity via Discord.</BR></BR>
</h2>Requirements</h2>
-> Python 3.0</BR>
-> discord.py version 1.5.1</BR>
-> subprocess32 version 3.5.4</BR>
-> nuclei</BR>

<h2>Installation</h2>
1. Clone the repository to your local machine.</BR>
2. Install the required packages:</BR>
  pip install -r requirements.txt</BR>
  <h2>Usage</h2>
  1. Run the tool:</BR>
  python main.py</BR>
  2. Enter the necessary information when prompted:</br>
Your Discord channel ID</br>
Your subdomain enumeration command</br>
Your directory enumeration command</br>
Your Discord token</br></br>
The tool will perform the subdomain and directory enumeration, run nuclei with the specified options, and send notifications to the Discord channel when any severity is discovered.</br>
<h2>Contributing</h2>
If you would like to contribute to the development of this tool, feel free to fork the repository and submit a pull request.
