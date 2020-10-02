""" add_photos.py is used to automatically create html code for each photo.
    TODO: find a way to do this for batches
    IDEA 1: - add photos to correct directory, i.e. kitchens, doors, etc.
            - scan directory to see if in html file
            - if not, create html snippet and add it
            - maybe scan /big/ and auto generate a cropped version for /small/
            - cropped photo dimsensions: 900 x 750
"""

# Template
# big_path: full image path
# small_path: thumbnail path
# caption: photo caption
# gallery_type: door, kitchen, window, more
TEMPLATE = """
          <div class="col-sm-6 col-md-4 col-lg-3 col-xl-2 item" data-aos="fade" data-src="big_path" data-sub-html="<h4>gallery_type</h4><p>caption</p>">
            <a href="#"><img src="small_path" alt="Image" class="img-fluid"></a>
          </div>
"""

def create_html_snippet(big_path, small_path, caption, gallery_type):
    """ Returns an html snippet for the photo using the template. """
    snippet = TEMPLATE.replace('big_path', big_path)
    snippet = snippet.replace('small_path', small_path)
    snippet = snippet.replace('caption', caption)
    snippet = snippet.replace('gallery_type', gallery_type)
    return snippet

def insert_html_snippet(html, snippet, index=108):
    """ Insert the snippet into the html file. """
    html.insert(index, snippet)
    return html

def get_html(path):
    """ Opens and returns the file at given path. """
    file = open(path, mode='r', encoding='utf-8')
    html = file.readlines()
    file.close()
    return html

def write_html(path, html):
    """ Write the new html code to the original file. """
    file = open(path, "w")
    file.writelines(html)
    file.close()

def main():
    pass

if __name__ == '__main__':
    main()
