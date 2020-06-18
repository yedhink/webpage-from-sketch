#!/usr/bin/env python
from __future__ import print_function
from __future__ import absolute_import

from argparse import ArgumentParser

from utils.training.CNNModel import *

VAL_SPLIT = 0.2


def build_parser():
    parser = ArgumentParser()
    parser.add_argument(
        '--training_dataset',
        type=str,
        dest='training_dataset',
        help='directory containing images and guis',
        required=True)
    parser.add_argument(
        '--validation_split',
        type=float,
        dest='validation_split',
        help='portion of training data for validation set',
        default=VAL_SPLIT)
    parser.add_argument(
        '--epochs',
        type=int,
        default=10,
        dest='epochs',
        help='number of epochs to train on',
        required=True)
    parser.add_argument(
        '--m_op_path',
        type=str,
        dest='m_op_path',
        help='directory for saving model data',
        required=True)
    parser.add_argument(
        '--m_json',
        type=str,
        dest='m_json',
        help='pretrained model json file',
        required=False)
    parser.add_argument(
        '--m_weight',
        type=str,
        dest='m_weight',
        help='pretrained model weights file',
        required=False)
    parser.add_argument(
        '--training_augmentation',
        type=int,
        dest='training_augmentation',
        help='use Keras image augmentation on training data',
        default=1)
    return parser


def main():

    parser = build_parser()
    options = parser.parse_args()
    training_dataset = options.training_dataset
    validation_split = options.validation_split
    epochs = options.epochs
    m_op_path = options.m_op_path
    m_json = options.m_json
    m_weight = options.m_weight
    training_augmentation = options.training_augmentation

    # Load model
    model = CNNModel(m_op_path, m_json, m_weight)

    # Create the model output path if it doesn't exist
    if not os.path.exists(m_op_path):
        os.makedirs(m_op_path)

    # Split the datasets and save down image arrays
    training_path, validation_path = ModelUtils.prepare_data_for_training(
        training_dataset, validation_split, training_augmentation)

    # Begin model training
    model.train(
        training_path=training_path,
        validation_path=validation_path,
        epochs=epochs)


if __name__ == "__main__":
    main()