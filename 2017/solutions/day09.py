


def main(inp):
    stream=list(inp)

    while '!' in stream:
        i=stream.index('!')
        stream.pop(i)
        stream.pop(i)
    garbage=0
    while '<' in stream:
        i=stream.index('<')
        j=stream.index('>')
        stream=stream[:i]+stream[j+1:]
        garbage+=j-i-1
  

    stream=[i for i in stream if i!=',']
    stream=''.join(stream)

    s=0
    while stream:
        i=stream.index('{}')
        stream=stream[:i]+stream[i+2:]
        s+=i+1


    return s,garbage
                