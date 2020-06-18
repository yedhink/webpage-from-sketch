#!/usr/bin/env python
import sys
import os
from argparse import ArgumentParser
from os.path import basename

from utils.sampling.Sampler import *


def build_parser():
    parser = ArgumentParser()
    parser.add_argument(
        '--input_img',
        type=str,
        dest='input_img',
        help='png filepath to convert into HTML',
        required=True)
    parser.add_argument(
        '--op_dir',
        type=str,
        dest='op_dir',
        help='dir to save generated gui and html',
        required=True)
    parser.add_argument(
        '--m_json',
        type=str,
        dest='m_json',
        help='trained model json file',
        required=True)
    parser.add_argument(
        '--m_weight',
        type=str,
        dest='m_weight',
        help='trained model weights file',
        required=True)
    parser.add_argument(
        '--style',
        type=str,
        dest='style',
        help='style to use for generation',
        default='default')
    parser.add_argument(
        '--print_generated_output',
        type=int,
        dest='print_generated_output',
        help='see generated GUI output in terminal',
        default=1)
    parser.add_argument(
        '--print_bleu_score',
        type=int,
        dest='print_bleu_score',
        help='see BLEU score for single example',
        default=0)
    parser.add_argument(
        '--original_gui_filepath',
        type=str,
        dest='original_gui_filepath',
        help='if getting BLEU score, provide original gui filepath',
        default=None)

    return parser


def main():
    parser = build_parser()
    options = parser.parse_args()
    input_img = options.input_img
    op_dir = options.op_dir
    m_json = options.m_json
    m_weight = options.m_weight
    style = options.style
    print_generated_output = options.print_generated_output
    print_bleu_score = options.print_bleu_score
    original_gui_filepath = options.original_gui_filepath

    if not os.path.exists(op_dir):
        os.makedirs(op_dir)

    sampler = Sampler(model_json_path=m_json, model_weights_path=m_weight)
    sampler.convert_single_image(
        op_dir,
        input_img=input_img,
        print_generated_output=print_generated_output,
        get_sentence_bleu=print_bleu_score,
        original_gui_filepath=original_gui_filepath,
        style=style)


if __name__ == "__main__":
    main()
