from glob import glob
import re
from PIL import Image
from tqdm import tqdm
import shutil
import inspect

# store builtin print
old_print = print


def new_print(*args, **kwargs):
    # if tqdm.tqdm.write raises error, use builtin print
    try:
        tqdm.write(*args, **kwargs)
    except ImportError:
        old_print(*args, **kwargs)


# globaly replace print with new_print
inspect.builtins.print = new_print


class GenDataset:
    def __init__(self, ASSETS_PATH, OUTPUT_PATH):
        self.background = Image.open(ASSETS_PATH + "white_background.png")
        self.gui_path = "../all_data/data/*.gui"
        self.row_count = 0

        self.header_btn = (ASSETS_PATH + "headers/header_button")
        self.row1_single = (ASSETS_PATH + "row1/first_row_single.png")
        self.row1_double = (ASSETS_PATH + "row1/first_row_double.png")
        self.row1_triple = (ASSETS_PATH + "row1/first_row_triple.png")
        self.row1_quad = (ASSETS_PATH + "row1/first_row_quad.png")

        self.row2_single = (ASSETS_PATH + "row2/second_row_single.png")
        self.row2_double = (ASSETS_PATH + "row2/second_row_double.png")
        self.row2_triple = (ASSETS_PATH + "row2/second_row_triple.png")
        self.row2_quad = (ASSETS_PATH + "row2/second_row_quad.png")

        self.row3_single = (ASSETS_PATH + "row3/third_row_single.png")
        self.row3_double = (ASSETS_PATH + "row3/third_row_double.png")
        self.row3_triple = (ASSETS_PATH + "row3/third_row_triple.png")
        self.row3_quad = (ASSETS_PATH + "row3/third_row_quad.png")

    def traverseFiles(self):
        count = 0
        for filename in tqdm(glob(self.gui_path)):
            self.row_count = 0
            self.background = Image.open(ASSETS_PATH + "white_background.png")
            print(f"""
                {filename} -> {OUTPUT_PATH}{count}.png
            """)
            count += 1
            with open(filename) as file:
                itr = 0
                lines = file.read().splitlines()
                length = len(lines)
                while itr < length:
                    if "header" in lines[itr]:
                        itr += (1)  # move to line with btn-inactive
                        btn_count = len(
                            re.findall(
                                "btn-inactive",
                                lines[itr],
                            ))
                        self.overlay(
                            btn_count,
                            f"{self.header_btn}_{btn_count}.png",
                        )
                        itr += (2)  # move to other containers after header
                    elif re.search(r"row", lines[itr]):
                        itr += 1
                        self.row_count += 1
                        if "double" in lines[itr]:
                            path_variable = getattr(
                                dataset_generator,
                                f"row{self.row_count}_double",
                            )
                            self.overlay(
                                btn_count,
                                path_variable,
                            )
                            itr += 6
                        elif ("single" in lines[itr]):
                            path_variable = getattr(
                                dataset_generator,
                                f"row{self.row_count}_single",
                            )
                            self.overlay(
                                btn_count,
                                path_variable,
                            )
                            itr += 4
                        elif ("triple" in lines[itr]):
                            path_variable = getattr(
                                dataset_generator,
                                f"row{self.row_count}_triple",
                            )
                            self.overlay(
                                btn_count,
                                path_variable,
                            )
                            itr += 10
                        elif ("quadruple" in lines[itr]):
                            path_variable = getattr(
                                dataset_generator,
                                f"row{self.row_count}_quad",
                            )
                            self.overlay(
                                btn_count,
                                path_variable,
                            )
                            itr += 13
                    else:
                        itr += 1
                    if itr + 4 > length:
                        break
                    print(f"""
                        {itr} < {length} : {lines[itr]}
                    """)
            self.background.show()
            if count == 1:
                break

    def overlay(self, times, fg_path):
        """
        foreground can be either of these:-
        1) header buttons - btn-inactive
        2) row1 - single, double, triple, quadruple
        3) row2 - single, double, triple, quadruple(optional)
        4) row3 - single, double, triple, quadruple(optional)

        First parameter to .paste() is the image to paste.
        Second are coordinates, and the secret
        sauce is the third parameter.
        It indicates a mask that will be used
        to paste the image.
        If you pass a image with transparency,
        then the alpha channel is used as mask.
        """
        foreground = Image.open(fg_path)
        self.background.paste(foreground, (0, 0), foreground)


if __name__ == "__main__":
    ASSETS_PATH = "../all_data/assets/try3/"
    OUTPUT_PATH = "../all_data/custom-generated/V3-custom-dataset/v3-hand-drawn-"
    dataset_generator = GenDataset(ASSETS_PATH, OUTPUT_PATH)
    dataset_generator.traverseFiles()
