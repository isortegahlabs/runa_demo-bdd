Feature:


Scenario:
  Given the URL "http://automation.runademos.info/"
  When we visit the site
  And we wait for the "welcome_messaage" element
  Given the username "producto+automation@runahr.com" and the password "runahr"
  When we make login successful