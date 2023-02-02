# Webpage From Sketch

Special kinda cooked ramen codebase. Use at your own discretion, because I neither me nor mere mortals can figure out what's going on in this codebase after a while!

## Authors
* @yedhink
* @ranjith

# Usage

```bash
pipenv shell # install the reqs
cd src
python train.py --training_dataset "dataset-path" --m_op_path "output-dir"
python3 sample.py --m_json "model" --op_dir "output-dir" --input_img "input-image" --m_weight "weights"
```
