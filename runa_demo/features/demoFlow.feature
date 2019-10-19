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
  And select option comenzar
  And open the detail of the first employee
  And modify the salary field with "5000" pesos
  And save employee changes
  And open the detail of the third employee
  And delete payroll employee
  And confirm delete payroll employee
  And continue step 2
  And unselect all
  And continue step 3
  And select section calculate
  And remove payroll
  And confirm delete payroll