# CS4320-Sem-Project
The project Nick Boland and Craig Lillemon have selected is a real estate management system. We will be attempting to streamline information that is relative to the owner or manager of the estate. With information that may place ease on the what actions may need to performed. Information such as rent, taxes of the property, a list of/amount of tenants, and more to be determines a the project is still in development. This can create an easier tracking system of the need if someone manages multiple properties and needs general or advance information of said properties




Developer Documentation: 
This project is open for anyone to modify or complete in their own way. However it should be noted that some features should be talked about for future understanding.
This project was designed for a model view template architecture, with the idea of people using it to store data and generate expense reports
The Project was also had an idea for client server however was not implemented in any way
The maintence record has a couple models that can be used for invoice, quotes and so on that was not implemented for the maintence records. It could be done in a similar way the expense reports and expense items was done if you were to attempt to do it on your own.,
The Project use Django for its model view template, and uses bootstrap 5 for the implementation of the nav bar and displaying the items. 
This project has a severe lack of CSS which can be done in order to make it look nicer, the part I would focus on first though is the forms, as it uses the django tables to auto generate them 
Some Key compenents to be aware of is Property is used in unit and expenses, and units contain a rental agreement, while the rental agreement contains the tenants. 
