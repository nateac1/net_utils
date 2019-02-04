def binary(ip, mask):
    vals = [128,64,32,16,8,4,2,1]
    ipbin = []
    maskbin = []
    count = 0
    subnet = 0
    for i in vals:
        if int(ip) >= i:
            ipbin.append(1)
            ip -= i
        elif int(ip) < i:
            ipbin.append(0)

        if int(mask) >= i:
            maskbin.append(1)
            mask -= i
        elif int(mask) < i:
            maskbin.append(0)
    for i in vals:
        if ipbin[count] == 1 and maskbin[count] == 1:
            subnet += i
        count += 1
    return subnet

def anding(ip=input("IP address: "), mask=input("Subnet mask: ")):
    ip = str(ip).split('.')
    mask = str(mask).split('.')
    net = []
    count = 0
    if not len(ip) == 4:
        print("That's an invalid IP address.")
    if not len(mask) == 4:
        print("That's an invalid subnet mask.")
    for j in mask:
        if not j == '255':
            net.append(str(binary(int(ip[count]), int(j))))
        elif j == '0':
            net.append('0')
        else:
            net.append(ip[count])
        count += 1
    print("The subnet for {} is: {}".format('.'.join(ip), '.'.join(net)))

anding()
