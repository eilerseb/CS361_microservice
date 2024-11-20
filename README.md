### Introduction:

This program is for filtering recipes based on a keyword given by the user. This microservice will read a txt file and then filter based on if the keyword is listed in the title of the recipe. It will then copy the recipes into another txt file where they can then be read. filter.py is set up to be continuously running in the back ground looking for any change to the unfiltered text file. 

### How to use:

1. Make sure that you have a text file for unfiltered recipes and a text filtered recipes.
2. Have your program write the recipes saved by user into the unfiltered recipes text file as well as the keyword they are search in the format of "keyword: " on the very last line of the text file. The microservice is designed to read it in that format.
3. Have microservice running.
4. Microservice will copy the recipes that match into the filtered recipes text file. Your program just needs to read that file.

** capitalization does not effect the microservice. 

### UML Sequence Diagram:
![image](https://github.com/user-attachments/assets/26050517-83c8-47d8-9344-0d95973069bb)
   
