def main():
    x = y = -1
    while True:
        x += 1
        y += 1
        if x is y:
            print('%d is %d' % (x, y))
        else:
            print('Attention! %d is not %d' % (x, y))
            break

    x = y = 0
    while True:
        x -= 1
        y -= 1
        if x is y:
            print('%d is %d' % (x, y))
        else:
            print('Attention! %d is not %d' % (x, y))
            break


if __name__ == '__main__':
    main()

# 上面代码的部分运行结果如下图所示。这个结果是因为CPython出于性能优化的考虑，把频繁使用的整数对象用一个叫small_ints的对象池缓存起来造成的。small_ints缓存的整数值被设定为[-5, 256]这个区间，也就是说，如果使用CPython解释器，在任何引用这些整数的地方，都不需要重新创建int对象，而是直接引用缓存池中的对象。如果整数不在该范围内，那么即便两个整数的值相同，它们也是不同的对象。
