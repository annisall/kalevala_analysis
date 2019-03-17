# Kalevala analysis

## kalevala_analysis.py file 
contains following functions:
* Loading poems under data-directory
* Cleaning poems: removing newlines, starting and trailing spaces, punctuations
* Statistics for poems:
	* For each poem: row count, word count
	* For each word within a poem: count and avg "waiting time" (word count between consecutive appearances of the same word within the poem. Not calculated for words occurring only once)
If results need to be printed, uncomment print calls at the end of the file

kalevala_analysis_test.py contains unit tests for the functions in kalevala_analysis.py file.

## kalevala_analysis.pynb
IN PROGRESS

