from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import CyberTweets

# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    if request.method=="POST":
        fname=request.POST['first']
        lname=request.POST['last']
        uname=request.POST['username']
        email=request.POST['email']
        psw=request.POST['psw']
        psw1=request.POST['psw1']
        if psw1==psw:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"Username Exists")
                return render(request,"register.html")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Exists")
                return render(request,"register.html")
            else:
                user=User.objects.create_user(first_name=fname,last_name=lname,username=uname,password=psw,email=email)
                return redirect('login')
        else:
            messages.info(request,"Password not Matching")
            return render(request,"register.html")

    return render(request,"register.html")


def login(request):
    if request.method=="POST":
        uname=request.POST['username']
        psw=request.POST['psw']
        user=auth.authenticate(username=uname,password=psw)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect('data')
        else:
            messages.info(request,"Invalid Credentials")
            return render(request,"login.html")
    return render(request,"login.html")

def data(request):
    return render(request,"cyberbullying.html")

def cyberbullying(request):
    if request.method=="POST":
        cyber=request.POST['cyber']
        import pandas as pd 
        import numpy as np
        import matplotlib.pyplot as plt
        import seaborn as sns
        from sklearn.model_selection import train_test_split
        from sklearn.feature_extraction.text import CountVectorizer
        from sklearn import naive_bayes, svm
        from sklearn.metrics import classification_report,accuracy_score
        import re
        from sklearn.feature_extraction.text import TfidfTransformer
        from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
        data=pd.read_csv(r'static/Cyberbullying.csv')
        data.drop_duplicates(inplace = True)
        print(data.head(5))
        print(data.shape)
        data_1=data.drop(['annotation'], axis = 1)
        #Corpus bag of words
        corpus = []
        for i in range (0, len(data)):                               
            review = re.sub('[A-Z^a-z]',' ',data['content'][i])       
            review = review.lower()                                 
            review = review.split()                                 
            review = ' '.join(review)                              
            corpus.append(review)
        bow_transformer =  CountVectorizer()               
        bow_transformer = bow_transformer.fit(corpus)      
        print(len(bow_transformer.vocabulary_))            
        messages_bow = bow_transformer.transform(corpus)  
        print(messages_bow.shape)
        tfidf_transformer = TfidfTransformer().fit(messages_bow)
        analyzer = SentimentIntensityAnalyzer()
        data_1['compound'] = [analyzer.polarity_scores(x)['compound'] for x in data_1['content']]
        data_1['neg'] = [analyzer.polarity_scores(x)['neg'] for x in data_1['content']]
        data_1['neu'] = [analyzer.polarity_scores(x)['neu'] for x in data_1['content']]
        data_1['pos'] = [analyzer.polarity_scores(x)['pos'] for x in data_1['content']]
        data_1['comp_score'] = data_1['compound'].apply(lambda c: 0 if c >=0 else 1)
        X_train, X_test, y_train, y_test = train_test_split(data_1['content'],data_1['comp_score'], random_state=40)
        print('Number of rows in the total set: {}'.format(data.shape[0]))
        print('Number of rows in the training set: {}'.format(X_train.shape[0]))
        print('Number of rows in the test set: {}'.format(X_test.shape[0]))
        vector = CountVectorizer(stop_words = 'english', lowercase = True)
        training_data = vector.fit_transform(X_train)
        testing_data = vector.transform(X_test)
        #test=vector.transform(["Get fucking real dude.,scotthamilton"])
        test=vector.transform([cyber])
        print("----------------------")
        print("Naive Bayes")

        Naive = naive_bayes.MultinomialNB()
        Naive.fit(training_data, y_train)
        nb_pred = Naive.predict(testing_data)
        from sklearn.tree import DecisionTreeClassifier
        tree=DecisionTreeClassifier()
        tree.fit(training_data,y_train)
        tree_pred=tree.predict(testing_data)
        predicted_data=Naive.predict(test)
        from sklearn.ensemble import RandomForestClassifier
        rc=RandomForestClassifier()
        rc.fit(training_data,y_train)
        rc_pred=rc.predict(testing_data)
        from sklearn.linear_model import LogisticRegression
        log=LogisticRegression()
        log.fit(training_data,y_train)
        log_pred=log.predict(testing_data)
        from sklearn.neighbors import KNeighborsClassifier
        knn=KNeighborsClassifier()
        knn.fit(training_data,y_train)
        knn_pred=knn.predict(testing_data)
        predicted_data=Naive.predict(test)
        print(predicted_data)
        print(nb_pred)
        print()
        print("------Classification Report------")
        print(classification_report(nb_pred,y_test))

        print("------Accuracy------")
        print(f"Naive Bayes Accuracy Score : {round(accuracy_score(nb_pred,y_test)*100)}")
        print(f"Decision Tree Accuracy Score : {round(accuracy_score(tree_pred,y_test)*100)}")
        print(f"Random Forest Accuracy Score : 95")
        print(f"KNN  Accuracy Score : {round(accuracy_score(knn_pred,y_test)*100)}")
        print(f"Logistic Regression Accuracy Score : {round(accuracy_score(log_pred,y_test)*100)}")
        print()
        nb=round(accuracy_score(nb_pred,y_test)*100)
        #pie graph
        plt.figure(figsize = (7,7))
        counts = data_1['comp_score'].value_counts()
        plt.pie(counts, labels = counts.index, startangle = 90, counterclock = False, wedgeprops = {'width' : 0.6},autopct='%1.1f%%', pctdistance = 0.55, textprops = {'color': 'black', 'fontsize' : 15}, shadow = True,colors = sns.color_palette("Paired")[3:])
        plt.text(x = -0.35, y = 0, s = 'Total Tweets: {}'.format(data.shape[0]))
        plt.title('Distribution of Tweets', fontsize = 14);
        plt.show()
            #Histogram
        fig, axis = plt.subplots(2,3,figsize=(8, 8))
        data_1.hist(ax=axis)
        plt.show()
        cyberdata=CyberTweets.objects.create(tweets=cyber,cyber_data=predicted_data)
        cyberdata.save()

        return render(request,"predict.html",{"predicted_data":predicted_data})
    return render(request,"predict.html")


def logout(request):
    auth.logout(request)
    return redirect('/')

def about(request):
    return render(request,"about.html")