
        fir_num = 0
        sec_num = 1 
        
        n = int(input("please enter your number series"))
        
        if n == 1:
            print(fir_num)
            
        elif n == 2:
            print(fir_num,' ',fir_num)
        
        else:
            print(fir_num,b, end=' ')
            for i in range (3,n+1):
                range_num = fir_num +  sec_num
                print( range_num, end=' ')
                fir_num =  sec_num
                sec_num =  range_num
                
