# Portfolio-site
Website showcasing various projects and things that I have created!


-To start the website go type cd "C:\Users\jesse\Desktop\Oozlys Website\myproject" then python manage.py runserver. Navigate to http://127.0.0.1:8000/.

Url map:
http://localhost:8000/ (Home for now)
http://localhost:8000/cybersecurity/

Roadmap for "The Outpost":

1.Compelete the  home page

2.add more content

3.Format the paragraphs better in html, (Bold letters paragraphing etc,)

4.create a better roadmap



To upload changes to the site: 
Clone the Repository to Your Local Machine:

Once your repository is created, you'll see instructions on how to clone it to your local machine. Copy the URL provided.
Open Terminal (or Command Prompt on Windows):

Navigate to the directory where you want to store your project files using the cd command.
Clone the Repository:

In the terminal, use the git clone command followed by the repository URL you copied earlier.
Example: git clone https://github.com/your-username/repository-name.git
Copy Your HTML File:

Place your HTML file inside the cloned repository folder on your local machine.
Add, Commit, and Push Your Changes:

Navigate into the cloned repository folder using the cd command.
Use the git status command to see the changes you've made.
Add your HTML file to the staging area using the git add command.
Commit your changes using the git commit command with a descriptive message.
Push your changes to GitHub using the git push command.
Example:
bash
Copy code
git add .
git commit -m "Add HTML file"
git push origin main
Verify on GitHub:

Go back to your repository on the GitHub website, and you should see your HTML file listed there.



<!-- Fifth row -->

<div class="w3-row" style="display: flex; justify-content: center; align-items: center;"><br>

  <div class="w3-quarter" style="display: flex; flex-direction: column; align-items: center;">
    <img src="{% static 'images/wizard.png' %}" alt="Boss1" style="width: 45%;" class="w3-circle w3-hover-opacity">
    <div style="text-align: center;">
      <h3>Jesse Larabie</h3>
      <p>Web Designer & Cyber security</p>
      <p>Expert schumer</p>
    </div>
  </div>

  <div class="w3-quarter" style="display: flex; flex-direction: column; align-items: center;">
    <img src="{% static 'images/nukee.webp' %}" alt="Boss1" style="width: 45%;" class="w3-circle w3-hover-opacity">
    <div style="text-align: center;">
      <h3>Johnathan Hienrick</h3>
      <p>Web Designer & Cyber security</p>
      <p>Expert gooner</p>
    </div>
  </div>

</div>


<!-- Modal popup for song selection -->
<div id="songModal" class="w3-modal">
    <div class="w3-modal-content w3-card-4">
      <header class="w3-container w3-teal">
        <span onclick="closeSongPopup()" class="w3-button w3-teal w3-display-topright">&times;</span>
        <h2>Choose a Song</h2>
      </header>
      <div class="w3-container">
        <div>
          <p>Minecraft</p>
          <ul>
            <li><a href="#" onclick="changeSong('{% static 'images/aria_math.mp3' %}'); return false;">Aria Math</a></li>
            <li><a href="#" onclick="changeSong('{% static 'images/wethands.mp3' %}'); return false;">Wet Hands</a></li>
            <li><a href="#" onclick="changeSong('{% static 'images/haggstrom.mp3' %}'); return false;">Haggstrom</a></li>
            <li><a href="#" onclick="changeSong('{% static 'images/haunt_muskie.mp3' %}'); return false;">Haunt Muskie</a></li>
            <li><a href="#" onclick="changeSong('{% static 'images/subwoofer.mp3' %}'); return false;">Subwoofer Lullaby</a></li>
          </ul>
        </div>
        <div>
          <p>Mario</p>
          <ul>
            <li><a href="#" onclick="changeSong('{% static 'images/Bowser_Peaches.mp3' %}'); return false;">Peaches (Mario Movie)</a></li>
            <li><a href="#" onclick="changeSong('{% static 'images/Super_mario_bros_theme_song.mp3' %}'); return false;">Super Mario Bros Theme Song (Super Mario World)</a></li>
            <li><a href="#" onclick="changeSong('{% static 'images/Piranha_Plants_Lullaby.mp3' %}'); return false;">Piranha Plant Lullaby (super mario 64)</a></li>
            <li><a href="#" onclick="changeSong('{% static 'images/Gelato_Beach.mp3' %}'); return false;">Gelato Beach (Super Mario Sunshine)</a></li>
            <li><a href="#" onclick="changeSong('{% static 'images/Gusty_Garden_Galaxy.mp3' %}'); return false;">Gusty Garden Galaxy (Super Mario Galaxy)</a></li>
            <li><a href="#" onclick="changeSong('{% static 'images/Night_Of_Doom_Bowsers_Sky_Palace_Theme.mp3' %}'); return false;">Night of doom boswer's theme (Super Mario 74)</a></li>
          </ul>
        </div>
        <div>
          <p>The Legend Of Zelda</p>
          <ul>
            <li><a href="#" onclick="changeSong('{% static 'images/lost_woods.mp3' %}'); return false;">Lost Woods (The Legend of Zelda: Ocarina Of Time)</a></li>
            <li><a href="#" onclick="changeSong('{% static 'images/Great_fairy.mp3' %}'); return false;">Great Fairy Fountain (The Legend of Zelda: Ocarina Of Time)</a></li>
            <li><a href="#" onclick="changeSong('{% static 'images/gerudo_valley.mp3' %}'); return false;">Gerudo Valley (The Legend of Zelda: Ocarina Of Time)</a></li>
            <li><a href="#" onclick="changeSong('{% static 'images/title_theme.mp3' %}'); return false;">Title Theme (The Legend of Zelda: Twilight Princess)</a></li>
            <li><a href="#" onclick="changeSong('{% static 'images/Midnas_Lament.mp3' %}'); return false;">Midna's Tament (The Legend of Zelda: Twilight Princess)</a></li>
            <li><a href="#" onclick="changeSong('{% static 'images/midnas_theme.mp3' %}'); return false;">Midna's Theme (The Legend of Zelda: Twilight Princess)</a></li>
            <li><a href="#" onclick="changeSong('{% static 'images/dragon.mp3' %}'); return false;">Dragon Roost Island (The Legend of Zelda: Windwaker)</a></li>
          </ul>
        </div>
        <p>Megaman</p>
          <ul>
            <li><a href="#" onclick="changeSong('{% static 'images/opening.mp3' %}'); return false;">Opening Theme (Megaman 8)</a></li>
            <li><a href="#" onclick="changeSong('{% static 'images/Title_Theme _megaman.mp3' %}'); return false;">Title Theme (Megaman 8)</a></li>
            <li><a href="#" onclick="changeSong('{% static 'images/Stage_Select1.mp3' %}'); return false;">Stage Select (Megaman 8)</a></li>
            <li><a href="#" onclick="changeSong('{% static 'images/Stage_Select_Sega_Genesis_remix.mp3' %}'); return false;">Stage Select Remix (Megaman 8)</a></li>
            <li><a href="#" onclick="changeSong('{% static 'images/Frost_Man.mp3' %}'); return false;">Frost Man Stage Theme (Megaman 8)</a></li>
            <li><a href="#" onclick="changeSong('{% static 'images/astro_man.mp3' %}'); return false;">Astro Man Stage Theme (Megaman 8)</a></li>
            <li><a href="#" onclick="changeSong('{% static 'images/Wily_Stage1.mp3' %}'); return false;">Wily Stage 1 (Megaman 8)</a></li>
          </ul>
        </div>
        <div>
      </div>
    </div>
  </div>
  













