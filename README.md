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














