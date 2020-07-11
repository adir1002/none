
try:
    with open('output.txt',wt) as strm:
        strm.write('ADIR GO AWAY!')
except IOError:
    print 'oops!'


'''
try:
    stream = open('Testy.txt','wrt')

    print(str(stream.writable()))
    stream.write('H')
    stream.writelines(['ello',' ','world'])
    stream.write('\n')
    #stream.close()

    #stream = open('Testy.txt','rt')
    print(stream.readable())
    print(stream.read(1))
    print(stream.readline())
    stream.close()

    #stream = open('Testy.txt','at')
    stream.write('demo!')
    stream.seek(0)
    stream.write('cool')
    #stream.flush()
    stream.close()
except:
    stream.close()
finally:
    x=1
'''
