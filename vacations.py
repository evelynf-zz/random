"{John,Tim,George} went on a {vacation,journey} to the {park, beach, castle}."

#Make a list of all of the possible sentences. 
def possible_sentences(string):
    #base case:
    if len(string) == 0:
        return [""]
    result = []
    start_option = string.find("{")
    
    #case 1
    if start_option == 0:
        end_option = string.find("}")
        new_string = string[1:end_option-1]
        poss_options = new_string.split(",")
        poss_strings = possible_sentences(string[end_option+1:))
        for option in poss_options:
            for poss_string in poss_strings:
                next_string = option + poss_string
                result.append(next_string)
    #case 2
    if start_option > 0:
        static_string = string[0:start_option-1]            
        poss_strings = possible_sentences(string[start_option:])
        for poss_string in poss_strings:
            next_string = static + poss_string
            result.append(next_string)
     
    #case 3
    if start_option < 0:
        return [string]
        
    return result
