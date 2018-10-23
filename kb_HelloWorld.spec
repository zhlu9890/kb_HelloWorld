/*
A KBase module: kb_HelloWorld
*/

module kb_HelloWorld {
    /*
        Insert your typespec information here.
    */
		
		typedef structure {
			string phrase;
		} InParams;
		typedef structure {
			string phrase;
		} OutParams;
		funcdef printhelloworld(InParams params)
			returns (OutParams) authentication required;
};
