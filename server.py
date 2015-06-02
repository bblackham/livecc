#!/usr/bin/env python

import web

urls = (
    "/", "Index",
    "/compile", "Compile",
)
app = web.application(urls, globals())

class Index:
    def GET(self):
        return web.redirect('/static/index.html')

    if __name__ == "__main__":
        app.run()

class Compile:
    def POST(self):
        import tempfile
        import os
        fd, filename = tempfile.mkstemp(suffix='.c')
        f = os.fdopen(fd, 'w')
        data = web.input()
        f.write(data['code'])
        f.close()
        obj_filename = filename[:-1]+'o'
        out_filename = filename[:-1]+'s'
        #os.spawnl(os.P_WAIT, '/usr/bin/gcc', '-O2', '-c', '-S', filename, '-o', out_filename)
        os.spawnl(os.P_WAIT, '/usr/bin/gcc', 'gcc', '-arch', 'armv5', '-O2', '-c', filename, '-o', obj_filename)
        os.system('gobjdump -dl %s > %s' % (obj_filename, out_filename))
        output = open(out_filename, 'r')
        data = output.read()
        output.close()
        os.unlink(filename)
        os.unlink(out_filename)
        return data

    if __name__ == "__main__":
        app.run()
