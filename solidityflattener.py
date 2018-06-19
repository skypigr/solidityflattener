import sys


class MergeSol():

    def __init__(self):
        self.order = list()
        self.fname = './ERC20Token.sol'
        self.target = './SingleFile.sol'

    def parseParameters(self):
        if len(sys.argv) < 3:
            print('ERROR: 3 or more arguments expected, %d were given' %
                  (len(sys.argv)-1))
            print('Usage: MergeSol source.sol newfile.sol')
            quit()
        else:
            self.fname = sys.argv[1]
            self.target = sys.argv[2]

    def getHeader(self):
        with open(self.fname) as f:
            content = f.readlines()
        validLine = 0
        for index, line in enumerate(content):
            if line[:6] == 'import':
                validLine = index
                break

        return ''.join(content[:validLine])

    def collectImportsFromFile(self, fname):
        with open(fname) as f:
            content = f.readlines()
        store = list()
        validLine = 0
        for index, line in enumerate(content):
            if line[:6] == 'import':
                # you may also want to remove whitespace characters
                # like `\n` at the end of each line
                l = line.strip()
                start = l.index('"', 0)
                end = l.index('"', start+1)
                path = l[start+1:end]
                store.append(path)
                validLine = index
            elif line[:6] == 'pragma':
                validLine = index

        validLine += 1
        if len(store) == 0:
            self.order.append((fname, validLine))
        else:
            for item in store:
                self.collectImportsFromFile(item)
            self.order.append((fname, validLine))

    def removeDuplicates(self):
        arr = self.order
        newStore = list()
        for item in arr:
            if item not in newStore:
                newStore.append(item)
        return newStore

    def printSeparateLine(self, filename):
        string = '\n' + '/' * 40 + ' ' + filename[2:] + ' ' + '/' * 40 + '\n'
        return string

    def generateSingleFile(self, importList):

        string = ''
        for item in importList:
            filename, index = item

            with open(filename) as f:
                content = f.readlines()
            string += self.printSeparateLine(filename)
            string += ''.join(content[index:])

        return string

    def writeToFile(self, string):
        with open(self.target, "w") as text_file:
            text_file.write(string)


def main():
    merger = MergeSol()
    merger.parseParameters()
    merger.collectImportsFromFile(merger.fname)
    imports = merger.removeDuplicates()
    for item in imports:
        print(item)
    string = merger.getHeader() + merger.generateSingleFile(imports)
    merger.writeToFile(string)


if __name__ == '__main__':
    main()
