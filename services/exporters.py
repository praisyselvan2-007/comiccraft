from pathlib import Path

from datetime import datetime

from fpdf import FPDF

from PIL import Image


EXPORTS_DIR = Path(
    "app/static/exports"
)


EXPORTS_DIR.mkdir(
    parents=True,
    exist_ok=True
)


def _text(value):

    return (

        str(value or "")

        .encode(
            "latin-1",
            "replace"
        )

        .decode("latin-1")

    )


def save_pdf(layout):

    filename = (

        "comiccraft_"

        f"{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        ".pdf"

    )


    path = EXPORTS_DIR / filename


    pdf = FPDF()


    pdf.set_auto_page_break(

        auto=True,

        margin=15

    )


    for panel in layout:

        pdf.add_page()


        # Panel heading
        pdf.set_font(

            "Helvetica",

            "B",

            18

        )


        pdf.cell(

            0,

            12,

            _text(

                f"Panel "
                f"{panel['panel_number']}: "
                f"{panel['title']}"

            ),

            ln=True

        )


        # Image path
        image_path = (

            Path("app")

            / "static"

            / panel["image"]

                .replace(
                    "/static/",
                    ""
                )

                .lstrip("/")

        )


        if image_path.exists():

            with Image.open(

                image_path

            ) as im:

                width, height = im.size


                max_width = 180

                max_height = 120


                scale = min(

                    max_width / width,

                    max_height / height

                )


                pdf.image(

                    str(image_path),

                    x=15,

                    y=35,

                    w=width * scale,

                    h=height * scale

                )


                y = (

                    35

                    + height * scale

                    + 8

                )

        else:

            y = 45


        pdf.set_xy(

            15,

            y

        )


        # Scene description
        pdf.set_font(

            "Helvetica",

            "I",

            10

        )


        pdf.multi_cell(

            180,

            6,

            _text(

                panel[
                    "scene_description"
                ]

            )

        )


        pdf.set_font(

            "Helvetica",

            "",

            11

        )


        pdf.ln(2)


        # Caption
        pdf.multi_cell(

            180,

            6,

            _text(

                panel["caption"]

            )

        )


        # Narration
        pdf.multi_cell(

            180,

            6,

            _text(

                panel["narration"]

            )

        )


        # Dialogue
        pdf.set_font(

            "Helvetica",

            "B",

            11

        )


        pdf.multi_cell(

            180,

            6,

            _text(

                panel["dialogue"]

            )

        )


    pdf.output(

        str(path)

    )


    return (

        f"/static/exports/"

        f"{filename}"

    )