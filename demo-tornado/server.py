import os
import random
import asyncio
from tornado.web import Application
from tornado.web import RequestHandler
from pyecharts import Scatter3D

REMOTE_HOST = "https://pyecharts.github.io/assets/js"


def scatter3d():
    data = [generate_3d_random_point() for _ in range(80)]
    range_color = [
        "#313695",
        "#4575b4",
        "#74add1",
        "#abd9e9",
        "#e0f3f8",
        "#fee090",
        "#fdae61",
        "#f46d43",
        "#d73027",
        "#a50026",
    ]
    scatter3D = Scatter3D("3D scattering plot demo", width=1200, height=600)
    scatter3D.add("", data, is_visualmap=True, visual_range_color=range_color)
    return scatter3D


def generate_3d_random_point():
    return [
        random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)
    ]


class DrawChartHandler(RequestHandler):
    async def get(self):
        s3d = scatter3d()
        self.render('pyecharts.html',
                    myechart=s3d.render_embed(),
                    host=REMOTE_HOST,
                    script_list=s3d.get_js_dependencies())


setting = {
    'template_path': os.path.join(os.path.dirname(__file__), "templates")
}

app = Application(
    [
        (r'/draw', DrawChartHandler)
    ], **setting
)
if __name__ == '__main__':
    app.listen(9999)
    ioloop = asyncio.get_event_loop()
    ioloop.run_forever()
