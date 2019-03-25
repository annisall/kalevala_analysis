# Kalevala analysis

This project analyses Kalevala poems. Poems are retrieved from [this site](http://runeberg.org/kalevala/) and files are assumed to be saved in separate files. Name of the files should correspond to the title in the web page. Files/Poems are assumed to be located under data directory.

There are three files related to analysis: kalevala_analysis.py, kalevala_analysis_test.py and kalevala_analysis.pynb. 

## kalevala_analysis.py 
Contains following functions:
* Loading poems under data-directory
* Cleaning poems: removing newlines, starting and trailing spaces, punctuations
* Statistics for poems:
	* For each poem: row count, word count
	* For each word within a poem: count and avg "waiting time" (word count between consecutive appearances of the same word within the poem. Not calculated for words occurring only once)
If results need to be printed, uncomment print calls at the end of the file

kalevala_analysis_test.py contains unit tests for the functions in kalevala_analysis.py file.

## kalevala_analysis.pynb
Contains following functions:
* Visulization of poem stats
* Finding keywords for each poem. Keyword is defined as word that appears in a poem, but is rare in other poems.
* Calculating and visualization of poem similarity

