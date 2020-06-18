# Webpage From Sketch
## Authors
* @ikigai
* @ranjith

# Usage
```bash
pipenv shell # install the reqs
cd src
python train.py --training_dataset "dataset-path" --m_op_path "output-dir"
python3 sample.py --m_json "model" --op_dir "output-dir" --input_img "input-image" --m_weight "weights"
```
