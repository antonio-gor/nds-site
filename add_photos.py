""" add_photos.py is used to automatically create html code for each photo.
    TODO: find a way to do this for batches
    IDEA 1: - add photos to correct directory, i.e. kitchens, doors, etc.
            - scan directory to see if in html file
            - if not, create html snippet and add it
            - maybe scan /big/ and auto generate a cropped version for /small/
            - cropped photo dimsensions: 900 x 750
"""
import os

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

HTML_DIRS = ["doors.html", "kitchens.html",
            "windows.html", "more.html"]

IMG_DIRS = ["images/doors/big", "images/kitchens/big",
            "images/windows/big", "images/more/big"]

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

def get_photos_in_dir(dir):
    """ Return list of jpgs in dir. """
    fnames = os.listdir(dir)
    return [fname for fname in fnames if "jpg" in fname]

def main():
    """ Scan each gallery dir and update html files with new imgs. """
    for html_dir, imgs_dir in zip(HTML_DIRS, IMG_DIRS):
        html = get_html(html_dir)
        imgs = get_photos_in_dir(imgs_dir)
        for img in imgs:
            if img not in ' '.join(html):
                big_path = imgs_dir + "/" + img
                small_path = big_path  # TODO: auto-create small version of img
                caption = html_dir.split('.')[0]
                gallery_type = caption
                snippet = create_html_snippet(big_path, small_path, caption, gallery_type)
                html = insert_html_snippet(html, snippet)
        write_html(html_dir, html)

if __name__ == '__main__':
    main()
