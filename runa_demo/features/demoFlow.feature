Feature:


Scenario:
  Given the URL "http://automation.runademos.info/"
  And the username "producto+automation@runahr.com" and the password "runahr"
  When we visit the site
  And we wait for the "welcome_messaage" element
  And we make login successful
  And we wait for the "closeModal_btn" element of modal
  And we close the modal for change the password
  And we create a new nomina manual
  And we are looking for the payroll group "QUESADILLAS"
  And we select day "01/06/2019"
  And select range of incidents "31/05/2019" to "06/06/2019"