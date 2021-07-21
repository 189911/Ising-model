      subroutine isi(T,nsteps,dev)
      real(kind=8),intent(in):: T
      integer(kind=8),intent(in):: nsteps
      real(kind=8),dimension(2),intent(out)::dev

      parameter (n=20)
      integer*1 is(n,n)
      real*8 dseed
      dimension histm(101),histe(101)
      data dseed /186761d0/

      nblock=10
      n2=n*n
      ama=0
      amaa=0
      ene=0
      enea=0
      do i=1,101
         histm(i)=0
         histe(i)=0
         end do
      do i =1,n
         do j=1,n
            is(i,j)=1
            call random_number(ran)
            if(ran.lt.0.5) is(i,j)=-1
            ama=ama+is(i,j)
            end do
         end do
      do i=1,n
         ip=i+1
         if(iip.gt.n) ip=1
         do j=1,n
            jp=jp+1
            if(jp.gt.n) jp=1
            ene=ene-is(i,j)*(is(ip,j)+is(i,jp))
            end do
         end do
      do k=1,nsteps/nblock
      do l=1,nblock

      do i=1,n
         do j=1,n
            sij=is(i,j)
            ip=i+1
            if(ip.gt.n) ip=1
            im=i-1
            if(im.lt.1) im=n
            jp=j+1
            if(jp.gt.n) jp=1
            jm=j-1
            if(jm.lt.1) jm=n
            de=2*sij*(is(ip,j)+is(im,j)+is(i,jp)+is(i,jm))
            call random_number (ran)
            if (exp(-de/T).gt.ran) then
               is(i,j)=-sij
               ama=ama-2*sij
               ene=ene+de
               end if
            end do
         end do
      end do
      enea=enea+ene
      amaa=amaa+ama
      im=(ama/n2+1)*0.5e2+1
      histm(im)=histm(im)+1

      ie=abs((ene/n2+2)*20.0+1)
      histe(ie)=histe(ie)+1
      end do

      miu=abs(amaa/(nsteps/nblock*n2))
      write(*,*) miu, energia
      energia=enea/(nsteps/nblock*n2)
      dev(1)=miu
      dev(2)=energia

      end subroutine
