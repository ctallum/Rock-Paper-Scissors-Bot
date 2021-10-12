import csv


fields = ['image_name', 'classification'] 
classifications = ["rock","paper","scissor"]

filename1 = "TrainDataset.csv"
with open(filename1, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 

    csvwriter.writerow(fields) 

    # loop through "rock", "paper", and "scissor"
    for classification in classifications:
        # each data set has 7 sub datasets
        for bunch in range(7):
            # each sub dataset has 120 photos
            # create list of numbers [001,002,...,119]
            image_number_set = [f"{i:03}" for i in range(120)]
            # loop through each number to form final image name
            for number in image_number_set:
                # example image name "rock01-001.png"
                image_name = f'{classification}0{bunch+1}-{number}.png'
                # write new row with image name and classification
                csvwriter.writerow([image_name,classification]) 

filename2 = "TestDataset.csv"
with open(filename2, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 

    csvwriter.writerow(fields) 

    # loop through "rock", "paper", and "scissor"
    for classification in classifications:
        # each data set has 4 sub datasets
        for bunch in range(4):
            # each sub dataset has 31 photos
            # create list of numbers [01,02,...,31]
            image_number_set = [f"{i:02}" for i in range(31)]
            # loop through each number to form final image name
            for number in image_number_set:
                # example image name "rock01-001.png"
                image_name = f'test{classification}0{bunch+1}-{number}.png'
                # write new row with image name and classification
                csvwriter.writerow([image_name,classification]) 