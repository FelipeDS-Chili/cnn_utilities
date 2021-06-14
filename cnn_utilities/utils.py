
import urllib.request
import os

######################################## METRICS #########################################################
def download_images(google_file, folder, root, output_height, output_width):

    ''''
    google_file: file where it is contained the cURLs text
    folder: image class folder
    root: root folder which contains all the images
    output_height: height wished for the image downloaded
    output_width: width wished for the image downloaded

    '''
    # Bajar fotos desde el archivo de google
    photos_urls = list()
    count = 1
    with open(google_file) as f:
        for line in f:
            start_index = line.find("https://encrypted-")
            if start_index != -1:
                end_index = line[start_index:].find("^")
                photos_urls.append(line[start_index:start_index+end_index])
            count += 1

    # Preprocesar imagenes
    try:
        os.mkdir(root+"/"+folder)
    except:
        pass
    try:
        os.mkdir(root+"/"+folder+"_prepro")
    except:
        pass
    count = 1
    for link in photos_urls:
        urllib.request.urlretrieve(link, root+"/"+folder+"/img"+str(count)+".jpg")
        count+= 1

    for filename in os.listdir(root+"/"+folder):
        try:
            image = Image.open(root+"/"+folder+"/"+filename)
            new_image = image.resize((output_width, output_height))
            new_image.save(root+"/"+folder+"_prepro/"+filename)
        except:
            pass
    return 'Done'



if __name__ == "__main__":
    pass










