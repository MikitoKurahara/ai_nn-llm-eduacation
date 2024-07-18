from flask import Flask, request, jsonify
from flask_cors import CORS
import k_nn

app = Flask(__name__)
CORS(app)

@app.route('/run_knn', methods=['POST'])
def run_knn():
    data = request.json
    k_value = data['k']
    distance_metric = data['distance_metric']
    
    # ここでK-NNの処理を行います
    new_image_path = '.\\PetImages\\test.jpg'
    predict=k_nn.k_nn_learning(k_value, distance_metric, new_image_path)
    
    result = {
        'message': f'K: {k_value}, 距離の計量法: {distance_metric} - 処理が完了しました
        あなたの画像は{predict[0]}点で{predict[1]}です'
    }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
