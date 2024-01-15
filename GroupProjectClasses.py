# Original File: id, unit_name, location, unit_type, price, min_nights, reviews_month, availability
# Feedback File: id, feedback
# User visit File: id, id_visit, location, location_visit, unit_type, unit_type_visit, price, price_visit

# class record to organize airbnb data
class airbnb_record:
    def __init__(record, unit_id, unit_name, location, unit_type, price, min_nights, reviews_month, availability):
        record.unit_id = unit_id
        record.unit_name = unit_name
        record.location = location
        record.unit_type = unit_type
        record.price = price
        record.min_nights = min_nights
        record.reviews_month = reviews_month
        record.availability = availability

class tag_record:
    def __init__(record, fb_unit_id, fb_tag):
        record.fb_unit_id = fb_unit_id
        record.fb_tag = fb_tag

# takes file as input, outputs a list of all the data organized, use comparisons against record.(what youre looking for) to search
def read_airbnb_record(filename):
    record_list = []
    for current_line in filename:
        #print(current_line)
        word_list = current_line.split("\t")
        airbnb = airbnb_record(word_list[0], word_list[1], word_list[2], word_list[3], word_list[4], word_list[5], word_list[6], word_list[7])
        record_list.append(airbnb)
    return record_list

def read_tag_record(filename):
    tag_list = []
    for current_line in filename:
        word_list = current_line.split("\t")
        user_tag = tag_record(word_list[0], word_list[1])
        tag_list.append(user_tag)
    return tag_list

def bubble_sort(compiled_list):
    #print(compiled_list)
    length = len(compiled_list)
    for i in range(0, length - 1):
        for j in range(0, length - i - 1):
            if compiled_list[j][0] > compiled_list[j + 1][0]:
                compiled_list[j], compiled_list[j + 1] = compiled_list[j + 1], compiled_list[j]
            
    return compiled_list


def float_bubble_sort(compiled_list):
    #print(compiled_list)
    length = len(compiled_list)
    for i in range(0, length - 1):
        for j in range(0, length - i - 1):
            if float(compiled_list[j][0]) > float(compiled_list[j + 1][0]):
                compiled_list[j], compiled_list[j + 1] = compiled_list[j + 1], compiled_list[j]
            
    return compiled_list


def find_listing(airbnb_rec):
    sorted_list = []
    matching_listings = []
    current_listing = ""

    print("Choose one of the following options:")
    print("(1) Recommend listings by price")
    print("(2) Recommend listings by popularity")
    print("(3) Recommend listings by location")
    print("(4) Recommend listings by type")
    print("(5) Recommend listings by tags")
    print("(6) Find a listing by ID")
    user_input = input("")

    if user_input == "1":
        
        compiled_records = []
         #should we print out all the listings or just the top 5 cheapest/most expensive
        for record in airbnb_rec:
            current_searched_record = []
            current_searched_record.append(int(record.price))
            current_searched_record.append(int(record.unit_id))
            compiled_records.append(current_searched_record)
        #print(compiled_records)
        sorted_listings = bubble_sort(compiled_records)
        #print(sorted_bubble)
        
        print("Would you like to search for:\n[1] cheapest\n[2] most expensive")
        price_search = input()
        if price_search == "1":
            for k in range(0, 5):
                current_id = sorted_listings[k][1]
                #print("* " + str(current_id))
                for record in airbnb_rec:
                    current_listing = ""
                    if record.unit_id == str(current_id):
                        current_listing = current_listing + "Unit ID: " + record.unit_id + ", " + record.unit_name
                        current_listing = current_listing + ", " + record.location + ", $" + record.price + " per night" + ", " + record.reviews_month + " reviews per month." 
                        matching_listings.append(current_listing)
                        #print("*" + current_listing)
            print("Here are the top 5 most budget friendly selections:")

        elif price_search == "2":
            for m in range(-1, -6, -1):
                current_id = sorted_listings[m][1]
                #print("* " + str(current_id))
                for record in airbnb_rec:
                    current_listing = ""
                    if record.unit_id == str(current_id):
                        current_listing = current_listing + "Unit ID: " + record.unit_id + ", " + record.unit_name
                        current_listing = current_listing + ", " + record.location + ", $" + record.price + " per night" + ", " + record.reviews_month + " reviews per month."
                        matching_listings.append(current_listing)
            print("Here are the top 5 priciest selections:")
        else:
            print("Error, invalid input.")


    if user_input == "2":
        compiled_records = []
        for record in airbnb_rec:
            current_searched_record = []
            current_searched_record.append(record.reviews_month)
            #print(current_searched_record)
            current_searched_record.append(int(record.unit_id))
            compiled_records.append(current_searched_record)
        sorted_listings = float_bubble_sort(compiled_records)
        #print(sorted_listings)
        for m in range(-1, -6, -1):
                current_id = sorted_listings[m][1]
                for record in airbnb_rec:
                    current_listing = ""
                    if record.unit_id == str(current_id):
                        current_listing = current_listing + "Unit ID: " + record.unit_id + ", " + record.unit_name
                        current_listing = current_listing + ", " + record.location + ", $" + record.price + " per night" + ", " + record.reviews_month + " reviews per month."
                        matching_listings.append(current_listing)
        print("Here are the top 5 most popular selections:")


    if user_input == "3":
        location_list = ["West End", "Kensington-Cedar Cottage", "Downtown Eastside", "Hastings-Sunrise", "Grandview-Woodland", "Renfrew-Collingwood", "Mount Pleasant", "Kitsilano", "Downtown", "Riley Park", "Arbutus Ridge", "Dunbar Southlands", "Killarney", "South Cambie", "Fairview"]
        for n in range(len(location_list)):
            number = n + 1
            print("[" + str(number) + "] " + location_list[n])
        location_input = int(input())
        if location_input > 15 or location_input < 1:
            print("Error, input not in range.")
        else:
            selected_location = location_list[location_input - 1]
            for record in airbnb_rec:
                    current_listing = ""
                    if record.location == selected_location:
                        current_listing = current_listing + "Unit ID: " + record.unit_id + ", " + record.unit_name
                        current_listing = current_listing + ", " + record.location + ", $" + record.price + " per night" + ", " + record.reviews_month + " reviews per month."
                        matching_listings.append(current_listing)
        print("Here are the selections within the location:")

    if user_input == "4":
        types_of_units = ["Entire home/apt", "Private room"]
        for o in range(2):
            print("[" + str(o + 1) + "] " + types_of_units[o])
        type_input = int(input())
        if type_input > 2 or type_input < 1:
            print("Error, input not in range.")
        else:
            selected_type = types_of_units[type_input - 1]
            for record in airbnb_rec:
                    current_listing = ""
                    if record.unit_type == selected_type:
                        current_listing = current_listing + "Unit ID: " + record.unit_id + ", " + record.unit_name
                        current_listing = current_listing + ", " + record.location + ", $" + record.price + " per night" + ", " + record.reviews_month + " reviews per month."
                        matching_listings.append(current_listing)
        
    if user_input == "5":
        print("Please choose from 4 tags:\n[1] Affordable\n[2] Accessable\n[3] Quirky\n[4] Clean")
        user_selection = input()
        if user_selection == "1":
            criteria = "Affordable"
        elif user_selection == "2":
            criteria = "Accessable"
        elif user_selection == "3":
            criteria = "Quirky"
        elif user_selection == "4":
            criteria = "Clean"
        else:
            print("Error, invalid input.")
        matching_listings = search_by_tag(criteria)
        #print(matching_listings)



    if user_input == "6":
        print("Please enter the listing ID:")
        search_id = input()
        for record in airbnb_rec:
            if record.unit_id == search_id:
                current_listing = current_listing + "Unit ID: " + record.unit_id + ", " + record.unit_name
                current_listing = current_listing + ", " + record.location + ", $" + record.price + " per night" 
                matching_listings.append(current_listing)
            else:
                print("There are no listings matching the entered ID.")
                break
    #print(matching_listings)
    return matching_listings


def search_by_tag(crit):
    matching_units_with_tags = []
    for tag in record_of_tags:
        current_listing = ""
        #print("user criteria:", str(crit))
        #print("record criteria:", str(tag.fb_tag))
        #print(str(crit) + str(tag.fb_tag) + "BLANK")
        if str(tag.fb_tag).strip("\n") == str(crit):
            current_listing = current_listing + "Unit ID: " + tag.fb_unit_id + ", Tag: " + str(tag.fb_tag).strip("\n")
            for record in record_of_airbnbs:
                if str(tag.fb_unit_id).strip("\n") == record.unit_id:
                    current_listing = current_listing + ", " + record.unit_name
                    current_listing = current_listing + ", " + record.location + ", $" + record.price + " per night" 
            matching_units_with_tags.append(current_listing)
    return matching_units_with_tags



# used ot filter out random inputs
def convert_user_tag(user_tag):
    try:
        valid_user_tag = int(user_tag)
    except:
        print("Sorry, this is not a valid input. Please try again.")
        convert_user_tag(user_tag)
    return valid_user_tag


# takes id as input, writes preselected feedback into a new file
def feedback(a_recs):

    feedback = ""
    f = open("tags.txt", "a")
    unit_id = input("Enter the ID of the listing:\n")
    print("Enter a tag for the listing. Choose from the following options:")
    print("[1] Accessible\n" + "[2] Affordable\n" + "[3] Quirky\n" + "[4] Clean\n")
    for record in a_recs:
        if unit_id == record.unit_id:
            current_id = unit_id
    input_tag = input()
    tag = convert_user_tag(input_tag)

    if tag == 1:
        feedback = "Accessible"
    elif tag == 2:
        feedback = "Affordable"
    elif tag == 3:
        feedback = "Quirky"
    elif tag == 4:
        feedback = "Clean"
    else:
        print("Error, the input is not valid")
    
    text = current_id + "\t" + feedback + "\n"
    f.write(text)
    f.close()
    print("Thank you for your feedback!")
    return


# OPERATOR -------------------------------------------------------------------------------------------------------------------------------
airbnb_file = open("airbnb_data.txt", "r")
tag_file = open("tags.txt", "r")
record_of_airbnbs = read_airbnb_record(airbnb_file)
record_of_tags = read_tag_record(tag_file)


print("Welcome to the CMPT 120 Airbnb Recommendation System!")
name = input("What is your name?\n")
print("Nice to meet you, " + name + "! How can we help you today?")

#for tag in record_of_tags:
    #print(tag.fb_tag)

while True:
    show_options = False
    result = []
    user_selection = ""
    print("Choose one of the following options:")
    print("(1) Provide feedback on a listing")
    print("(2) Find a listing")
    print("(3) Quit")
    user_input = input("")
    if user_input == "3":
        print("Goodbye, " + name + "!") # i dont think we should directly print from the function, rather assign it to a variable and return it
        airbnb_file.close()
        tag_file.close()
        break
    elif user_input == "2":
        result = find_listing(record_of_airbnbs)
        show_options = True
    elif user_input == "1":
        result = feedback(record_of_airbnbs)

    else:
        print("Invalid response. Please choose option 1, 2, or 3.")

    if result == []:
        print("There are no selections that fit your criteria.")
        airbnb_file.close()
        tag_file.close()
        break


    if show_options == True:
        selection_options = len(result)
        for q in range(0, selection_options):
            option = q + 1
            print("[" + str(option) + "] " + result[q])
        print("Please select from the above options")
        user_option_selection = int(input())


        """
        user_selection = selection_options[user_option_selection + 1]
        print("Error, invalid input.")
        airbnb_file.close()
        tag_file.close()
        break
        """
    

        user_selection = result[user_option_selection - 1]
        print("You have selected: " + user_selection)
        print("Would you like to keep browsing?:\n[1] Yes\n[2] No")
        to_quit = input()
        if to_quit == "2":
            print("Goodbye, " + name + "!")
            airbnb_file.close()
            tag_file.close()
            break


"""
# debugging stuff
file = "airbnb_data.txt"
record_of_airbnbs = read_airbnb_record(file)
result = find_listing(record_of_airbnbs)
for l in range(len(result)):
    print(result[l])
"""