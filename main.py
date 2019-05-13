import math


def calc_angle_mbc(a, b):
    """ Metodo que calular o valor do angulo da media da hipotenusa, 
    esse metodo é mais ditatico e utiliza os principios ensinados ao alunos do
    7ª série/8º ano e 8ª série/9º ano
    """

    # Calular hipotenusa h² = a² + b²
    h = math.sqrt((a ** 2) + (b ** 2))

    # valor da Mediana: AM = BC/2
    mediana = h / 2

    # Cossenos invertido (αa = arc_cos a2 – b2 – c2 / – 2.b.c)
    arc_cos_b = ((b ** 2) + (mediana ** 2) - (mediana ** 2)) / (2 * b * mediana)

    # Calcula o Cosseno em Radianos
    cos_b = math.acos(arc_cos_b)

    # Converte Radianos em Graus
    graus = math.degrees(cos_b)

    return int(round(graus))
