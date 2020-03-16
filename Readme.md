
# ![Jaspex](static/images/logoNav.PNG?raw=true "Title")
>This repository is for the Online Json to <a href="https://jaspex.herokuapp.com/">Apex conversion tool</a>.

>This tool Converts JSON into the Apex JSON Generator Class code.

---

# _How it works:_

- Go to the Tool hosted on the Heroku <a href="https://jaspex.herokuapp.com/">here</a>.

- Paste your JSON code into the first box.

- Submit the input using "Generate Apex" button.

- Copy your apex method.
>

  ![Conversion Tutorial](static\images\normalConversion.gif)

>

- Paste it inside your class and call it inside your logic.

---

---

# _Other Features:_

- Convert Quoted JSON into Apex JSON Generator class obj.

>

  ![Quoted JSON Conversion](static\images\quoteConversion.gif) 

>

# _JSON GENERATOR over JSON?_

- Since the JSON encoding that's generated by Apex through the serialization method in the System.JSON class 
  isn't identical to the standard JSON encoding in some cases, the System.JSONGenerator class is provided 
  to enable the generation of standard JSON-encoded content.
  
- The System.JSONGenerator class is provided to enable the generation of standard JSON-encoded content and 
  gives you more control on the structure of the JSON output.
  
- There are less chances of having an Structure problem in your hardcoded json response if it is build using 
  the Generator class.
  
- You can check if you response is properly closed or not using generator class's function "isClosed()".

- This class is very useful if you are creating a Mock class which uses the JSON response. So you either 
  write whole JSON( and cover it between single inverted commas ! ) or you use Static resources method. 
  Using the JSON generator in this case will make you code look good and there are less chances of any 
  exceptions occurrence.

---
  
# Support
Reach out to me at one of the following places!
- <a href="https://twitter.com/AyushSh06594329" target="_blank">Twitter</a>
- <a href="https://www.linkedin.com/in/ayush-sharma-%E2%98%81-75b55613a/" target="_blank">Linkedin</a>
- <a href="https://github.com/ayushsharma84444" target="_blank">Github Profile</a>

---

# License
- <a href="http://opensource.org/licenses/mit-license.php" >MIT license</a>  
