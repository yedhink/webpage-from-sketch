from __future__ import absolute_import

from utils.dataset.Dataset import *


class ModelUtils:
    @staticmethod
    def prepare_data_for_training(data_input_folder, validation_split,
                                  training_augmentation):

        dataset = Dataset(data_input_folder)
        training_path, validation_path = dataset.split_datasets(
            validation_split)
        dataset.preprocess_data(training_path, validation_path,
                                training_augmentation)

        return training_path, validation_path