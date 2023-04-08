from flask import Flask, render_template, url_for, request
import string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('mapage.html')

@app.route('/', methods=['POST','GET'])
def upload_file():
    if  request.method == 'POST':
        uploaded_file = request.files['cv-txt']
       
       
        data = uploaded_file.read().decode('Latin-1')


        selected_competences = request.form.getlist("competence")
        #turn the selected competences list to a set so we can compare it with the one in the file easily
        selected_competences = set(selected_competences)

        print(selected_competences)
        #traitement sur les mots clés
        #enlève ponctuation
        punctuation = set(".;,?!:-_\’'\n\t’"+ string.punctuation)

        #mets tout en minuscule
        data = data.lower()

        for p in punctuation:
            data = data.replace(p," ")

        #Découpe la chaine de caractère en mots
        wordscv = data.split()

        # Enlève les doublons
        words_cv_unique = set(wordscv)
       
        
        competences_of_interest = words_cv_unique.intersection(selected_competences)
        
        return render_template("matches.html",competences_of_interest = competences_of_interest)
    

    #GET
    return render_template("mapage.html")

@app.route('/paysContinent', methods=['POST'])
def search():
    url = 'https://api.emploi-store.fr/partenaire/offresdemploi/v2/offres/search?paysContinent=XX'
    if request.method == 'POST':
        continentquery = request.form['continentquery']
        data = [continentquery]
    return render_template('results.html')
    
@app.route('/query-example')
def query_example():
    return 'Query String Example'

@app.route('/form-example')
def form_example():
    return 'Form Data Example'

@app.route('/json-example')
def json_example():
    return 'JSON Object Example'

if __name__ == '__main__':
   
    app.run(debug=True,)

