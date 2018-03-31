# We import the media file containing the Movie class
# And the fresh_tomatoes file containing the open_movies_page method
import media
import fresh_tomatoes

# Here, we instantiate a set of movie objects using Movie class from media.py
mother = media.Movie(
        "Mother!",
        "A couple's relationship is tested when uninvited guests arrive at their home, disrupting their tranquil existence.",
        "http://cdn.collider.com/wp-content/uploads/2017/08/mother-poster-javier-bardem.jpg",
        "https://youtu.be/XpICoc65uh0")

araya = media.Movie(
        "Araya",
        "Araya is an old natural salt mine located in a peninsula in northeastern Venezuela which was still, by 1959, being exploited manually five hundred years after its discovery by the Spanish.",
        "https://cdn.shopify.com/s/files/1/0150/7896/products/ARAYA_1024x1024.jpg?v=1332339521",
        "https://youtu.be/-tggEMhCVhc")

babadook = media.Movie(
        "The Babadook",
        "A widowed mother, plagued by the violent death of her husband, battles with her son's fear of a monster lurking in the house, but soon discovers a sinister presence all around her.",
        "http://ratpackpodcasts.com/WP-Files/wp-content/uploads/Babadook-Poster.jpg",
        "https://youtu.be/vAV3JZY3Kqs")

junglebook = media.Movie(
        "The Jungle Book",
        "Bagheera the Panther and Baloo the Bear have a difficult time trying to convince a boy to leave the jungle for human civilization.",
        "https://ia.media-imdb.com/images/M/MV5BMjAwMTExODExNl5BMl5BanBnXkFtZTgwMjM2MDgyMTE@._V1_UY268_CR0,0,182,268_AL_.jpg",
        "https://youtu.be/LNVTKXIK7q8")

bladerunner = media.Movie(
        "Blade Runner",
        "A blade runner must pursue and try to terminate four replicants who stole a ship in space and have returned to Earth to find their creator.",
        "https://cdn2.bigcommerce.com/server5000/yshlhd/products/8895/images/129622/full_bladerunner_8772__41523.1512009707.1280.1280.jpg?c=2",
        "https://youtu.be/eogpIG53Cis")


# We put the Movie objects into an array
all_movies = [mother, araya, babadook, junglebook, bladerunner]

# We pass the array to the open_movies_page method from the fresh_tomatoes file
fresh_tomatoes.open_movies_page(all_movies)
