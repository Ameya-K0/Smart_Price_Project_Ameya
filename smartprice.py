import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

def load_data():
    DF = pd.read_csv('data.csv')
    encoder = LabelEncoder() #from sklearn.preprocessing
    DF['category_num'] = encoder.fit_transform(DF["category"]) #should turn categorys A-C to 0-2

    x = DF[['size_cm', 'brand_rating', 'category_num']]
    y = DF['price']

    return x, y, encoder

def model_train(x, y):

    model = LinearRegression()
    model.fit(x, y) #fit calculates best slope and intercept values to help with prediction
    return model 

def user_input(encoder):
    size = float(input("Please enter your product's size (cm):"))
    rating = int(input("Please enter your product's brand rating (1-5):"))
    category = input("Please enter your product's category:")

    category_num = encoder.transform([category])[0]

    return size, rating, category_num

def price_prediction(model, size, rating, category_num):
    
    input_group = [[size, rating, category_num]]
    predicted_price = model.predict(input_group)
    
    return predicted_price[0] #use our model to predict the price 

def main():
    x, y, encoder = load_data()
    model = model_train(x,y)
    size, rating, category = user_input(encoder)
    price = price_prediction(model, size, rating, category)
    print("Predicted price: %f$" % price)
    

if __name__ == "__main__": #to start main
    main()