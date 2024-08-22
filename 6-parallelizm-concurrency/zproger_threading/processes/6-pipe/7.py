import time

from multiprocessing import Pipe, Process


def getter(pipe):
    out, inp = pipe
    inp.close()         # данный процесс сможет только читать данные, т.к. передачу данных запретили (закрывается только в текущем процессе - локально)
    while True:
        try:
            print('data:', out.recv())  # recv() - блокирующий метод, остановит код процесса в этом месте, пока не получит новые данных
        except:
            break


def setter(sequence, input_c):
    for item in sequence:
        time.sleep(1)
        input_c.send(item)



def main():
    output_c, input_c = Pipe()
    g = Process(target=getter, args=((output_c, input_c),))
    g.start()

    setter([1, 2, 3, 4, 5], input_c)
    output_c.close()  # закроется только в этом процессе
    input_c.close()






if __name__ == '__main__':
    main()


