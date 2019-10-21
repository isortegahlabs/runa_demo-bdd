Feature: Technical test implementing behave with python, on the RUNA project platform.
  The test is grouped in scenarios only for better reading and interpretation

Scenario: Enter the RUNA page and login successfully.
  Given the URL "http://automation.runademos.info/"
  And the username "producto+automation@runahr.com" and the password "runahr"
  When visit the site
  And wait for the "welcome_messaage" element
  Then the login page is seen
  When make login successful
  And wait for the "change_modal_password_title" element
  Then the login was successful

Scenario: Close modal of password change and create manual payroll.
  When wait for the "closeModal_btn" element of modal
  And close the modal for change the password
  And create a new nomina manual
  And looking for the payroll group "QUESADILLAS"
  And select day "01/06/2019"
  And select range of incidents "31/05/2019" to "06/06/2019"
  And wait for the "activepayroll_title" element in nomina page
  Then payroll creation was successful

Scenario: Start operating the payroll and edit 1 of the employees.
  When select option comenzar
  And wait for the "assertsectioncalculate" element in nomina page
  And wait for the "first_employee_txt" element in nomina page
  And open the detail of the first employee
  And modify the salary field with "5000" pesos
  And wait for the "savesalary_btn" element in nomina page
  And save employee changes
  And wait for the "first_employee_txt" element in nomina page
  Then the new salary is $5,000.00

Scenario:Remove an employee and verify the removal.
  When open the detail of the third employee
  And delete payroll employee
  And confirm delete payroll employee
  Then only 4 employees left

Scenario: Make adjustments to the payroll and remove it, in addition to logging out.
  When continue step 2
  And unselect all
  And continue step 3
  And select section calculate
  And remove payroll
  And confirm delete payroll
  And select option ADMINISTRADOR
  And select option CERRAR SESION
  And wait for the "welcome_messaage" element
  Then the login page is seen