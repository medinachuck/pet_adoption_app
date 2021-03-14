def predict_single(img_file):
    'function to take image and return prediction'
    prediction = learn.predict(open_image(img_file))
    probs_list = prediction[2].numpy()
    return {
        'category': classes[prediction[1].item()],
        'probs': {c: round(float(probs_list[i]), 5) for (i, c) in enumerate(classes)}
    }