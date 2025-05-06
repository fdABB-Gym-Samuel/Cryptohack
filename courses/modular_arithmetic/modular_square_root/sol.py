# In a congruence of the form r^2 ≡ a mod p, Tonelli-Shanks calculates r.

a = 8479994658316772151941616510097127087554541274812435112009425778595495359700244470400642403747058566807127814165396640215844192327900454116257979487432016769329970767046735091249898678088061634796559556704959846424131820416048436501387617211770124292793308079214153179977624440438616958575058361193975686620046439877308339989295604537867493683872778843921771307305602776398786978353866231661453376056771972069776398999013769588936194859344941268223184197231368887060609212875507518936172060702209557124430477137421847130682601666968691651447236917018634902407704797328509461854842432015009878011354022108661461024768
p = 30531851861994333252675935111487950694414332763909083514133769861350960895076504687261369815735742549428789138300843082086550059082835141454526618160634109969195486322015775943030060449557090064811940139431735209185996454739163555910726493597222646855506445602953689527405362207926990442391705014604777038685880527537489845359101552442292804398472642356609304810680731556542002301547846635101455995732584071355903010856718680732337369128498655255277003643669031694516851390505923416710601212618443109844041514942401969629158975457079026906304328749039997262960301209158175920051890620947063936347307238412281568760161


def tonelli_shanks(a: int, p: int) -> int:
    """
    Function to solve the equation x^2 = a (mod p) using the Tonelli-Shanks algorithm.
 
    Parameters:
    - a: int
        The value of 'a' in the equation.
    - p: int
        The prime number 'p' in the equation.
 
    Returns:
    - int:
        The solution 'x' to the equation x^2 = a (mod p).
 
    Raises:
    - ValueError:
        Raises an error if 'p' is not an odd prime or if 'a' is not a quadratic residue modulo 'p'.
    """
 
    # Checking if 'p' is an odd prime
    if p <= 2 or p % 2 == 0:
        raise ValueError("'p' must be an odd prime number.")
 
    # Checking if 'a' is a quadratic residue modulo 'p'
    if pow(a, (p - 1) // 2, p) != 1:
        raise ValueError("'a' is not a quadratic residue modulo 'p'.")
 
    # Step 1: Finding 'q' and 's' such that p - 1 = q * 2^s
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
 
    # Step 2: Finding a non-quadratic residue 'z' modulo 'p'
    z = 2
    while pow(z, (p - 1) // 2, p) == 1:
        z += 1
 
    # Step 3: Initializing variables
    x = pow(a, (q + 1) // 2, p)
    b = pow(a, q, p)
    g = pow(z, q, p)
    r = s
 
    # Step 4: Main loop
    while True:
        if b == 1:
            return x
 
        # Finding the smallest 'm' such that b^(2^m) = 1 (mod p)
        m = 0
        while pow(b, 2 ** m, p) != 1:
            m += 1
 
        # Step 4a: Updating variables
        gs = pow(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m
 
    return x  # This line is not necessary, as the function will always return in the while loop

print(tonelli_shanks(a, p))