#coding=utf-8
import os,sys
fastqfile=sys.argv[1] ### Raw fastq file,less than 500Mb is better
#from Bio import pairwise2, SeqIO
list=[]
out=open('countA_{0}.xls'.format(fastqfile),'w')
out.write('rerads id\tpercentA\tAAAAA\n')
outseq=open('cut_{0}'.format(fastqfile),'w')
#for record in SeqIO.parse(fastqfile, "fastq"):
number=0
count=0
if 2>1:
	fastq=open(fastqfile).readlines()
	if len(fastq)/4.!=len(fastq)//4:
		exit('fuck you!!')
	else:
		print len(fastq)/4
		for eachfour in range(0,len(fastq)+4,4)[1:]:
			outseq.write(fastq[eachfour-4])
			seq=fastq[eachfour-3]
			
			cut_head=seq[8:];allA=cut_head.count('A')
			if round(float(allA)/len(cut_head),3)>0.3:
				out.write('\t'.join([fastq[eachfour-4].strip(),str(round(float(allA)/len(cut_head),3))])+'\t')
			else:
				pass
			tailx=seq[len(seq)-len(seq)/2:];taily=seq[len(seq)-len(seq)/4:]
			if tailx.count('AAAAA')>2 or taily.count('AAAAA')>1:
				number+=1
				#print tailx.count('AAAAA')
				#print taily.count('AAAAA')
				sed=100
				for each in range(0,sed):
					if seq.count('AAAAA'+each*'A')==0:
						count+=1
						AA='AAAAA'+(each-1)*'A'
						print AA
						out.write(AA+'\n')	
						if AA in tailx or AA in taily:
							outseq.write(cut_head.split(AA)[0]+'\n')
						else:
							#print seq;print tailx;print taily
							outseq.write(cut_head+'\n')
							print ('fuck, %s seq has too many A!'%(fastq[eachfour-4]))
						break
			else:
				#outseq.write(cut_head+'\n')
				outseq.write(cut_head)
			outseq.write(fastq[eachfour-2])
			outseq.write(fastq[eachfour-1])
					
outseq.close();out.close()	 
print number,count
