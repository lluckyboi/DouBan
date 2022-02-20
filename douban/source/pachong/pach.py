from lxml import etree
xml = """
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35144311/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35144311">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2702755317.jpg" alt="��ʨ����" data-x="8268" data-y="11576">
                
            </div>
            <p>
                

                ��ʨ����

                
                    <strong>8.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34990918/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="true" data-id="34990918">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2673290266.jpg" alt="�հ�" data-x="1052" data-y="1499">
                
            </div>
            <p>
                
                    <span class="green">
                        <img src="https://img3.doubanio.com/f/movie/caa8f80abecee1fc6f9d31924cef8dd9a24c7227/pics/movie/ic_new.png" width="16" class="new">
                    </span>
                

                �հ�

                
                    <strong>7.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35045591/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="true" data-id="35045591">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2808318200.jpg" alt="���������󹦴��Ӱ" data-x="672" data-y="1000">
                
            </div>
            <p>
                
                    <span class="green">
                        <img src="https://img3.doubanio.com/f/movie/caa8f80abecee1fc6f9d31924cef8dd9a24c7227/pics/movie/ic_new.png" width="16" class="new">
                    </span>
                

                ���������󹦴��Ӱ

                
                    <strong>7.1</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35422807/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35422807">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2724443759.jpg" alt="��������" data-x="2088" data-y="3000">
                
            </div>
            <p>
                

                ��������

                
                    <strong>7.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/27605105/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="27605105">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2757579107.jpg" alt="������ħ" data-x="2765" data-y="4096">
                
            </div>
            <p>
                

                ������ħ

                
                    <strong>6.7</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/3078409/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="3078409">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2701416129.jpg" alt="�ųۼ���" data-x="1013" data-y="1500">
                
            </div>
            <p>
                

                �ųۼ���

                
                    <strong>6.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35242938/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35242938">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2678037153.jpg" alt="�ٲ�" data-x="1448" data-y="2048">
                
            </div>
            <p>
                

                �ٲ�

                
                    <strong>7.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35068653/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35068653">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2770857575.jpg" alt="��ɱ2" data-x="9999" data-y="14004">
                
            </div>
            <p>
                

                ��ɱ2

                
                    <strong>5.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34447553/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34447553">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2669034145.jpg" alt="��������������" data-x="595" data-y="842">
                
            </div>
            <p>
                

                ��������������

                
                    <strong>7.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35437945/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="true" data-id="35437945">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2641407927.jpg" alt="����֮������" data-x="1080" data-y="1920">
                
            </div>
            <p>
                
                    <span class="green">
                        <img src="https://img3.doubanio.com/f/movie/caa8f80abecee1fc6f9d31924cef8dd9a24c7227/pics/movie/ic_new.png" width="16" class="new">
                    </span>
                

                ����֮������

                
                    <strong>7.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35235502/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35235502">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2639821491.jpg" alt="��ʻ�ҵĳ�" data-x="2000" data-y="2829">
                
            </div>
            <p>
                

                ��ʻ�ҵĳ�

                
                    <strong>8.0</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34884712/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34884712">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2730833093.jpg" alt="��Ҫ̧ͷ" data-x="1080" data-y="1920">
                
            </div>
            <p>
                

                ��Ҫ̧ͷ

                
                    <strong>7.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30300279/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30300279">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2586398074.jpg" alt="����������" data-x="4048" data-y="6285">
                
            </div>
            <p>
                

                ����������

                
                    <strong>7.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/3001114/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="3001114">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2687443734.jpg" alt="ɳ��" data-x="2764" data-y="4096">
                
            </div>
            <p>
                

                ɳ��

                
                    <strong>7.7</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35652715/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35652715">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2734251152.jpg" alt="��������ķ" data-x="1000" data-y="1500">
                
            </div>
            <p>
                

                ��������ķ

                
                    <strong>8.7</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30223888/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30223888">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2677303737.jpg" alt="������" data-x="1688" data-y="2500">
                
            </div>
            <p>
                

                ������

                
                    <strong>5.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/33437152/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="33437152">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2678298618.jpg" alt="Ȯ֮��" data-x="1500" data-y="2222">
                
            </div>
            <p>
                

                Ȯ֮��

                
                    <strong>7.7</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35258381/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35258381">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2717809625.jpg" alt="������" data-x="2000" data-y="3000">
                
            </div>
            <p>
                

                ������

                
                    <strong>7.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35294995/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35294995">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2683055011.jpg" alt="�Һ��ҵĸ���" data-x="2857" data-y="4000">
                
            </div>
            <p>
                

                �Һ��ҵĸ���

                
                    <strong>6.5</strong>
                
            </p>
        </a><a class="item" target="_blank" href="https://movie.douban.com/subject/35286583/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35286583">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2666651888.jpg" alt="����С�£����ţ���֮���´��ղ�ѧԺ" data-x="1000" data-y="1414">
                
            </div>
            <p>
                

                ����С�£����ţ���֮���´��ղ�ѧԺ

                
                    <strong>9.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26962981/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="26962981">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2732782860.jpg" alt="���ֺ�����2" data-x="1012" data-y="1500">
                
            </div>
            <p>
                

                ���ֺ�����2

                
                    <strong>7.1</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/25845392/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="25845392">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2681329386.jpg" alt="�����" data-x="1080" data-y="1513">
                
            </div>
            <p>
                

                �����

                
                    <strong>7.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26897885/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="26897885">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2721066869.jpg" alt="����" data-x="720" data-y="1080">
                
            </div>
            <p>
                

                ����

                
                    <strong>8.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35134724/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35134724">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2807936075.jpg" alt="ħ������" data-x="3000" data-y="4188">
                
            </div>
            <p>
                

                ħ������

                
                    <strong>6.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26996619/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="26996619">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2734316987.jpg" alt="�Ŷ����о�" data-x="1785" data-y="2500">
                
            </div>
            <p>
                

                �Ŷ����о�

                
                    <strong>5.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34801038/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34801038">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2844387600.jpg" alt="�ڿ͵۹�����������" data-x="4000" data-y="5929">
                
            </div>
            <p>
                

                �ڿ͵۹�����������

                
                    <strong>5.7</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30279170/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30279170">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2690712224.jpg" alt="����ʱ��" data-x="1500" data-y="2222">
                
            </div>
            <p>
                

                ����ʱ��

                
                    <strong>8.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35360296/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35360296">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2687984714.jpg" alt="żȻ������" data-x="1460" data-y="2064">
                
            </div>
            <p>
                

                żȻ������

                
                    <strong>8.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35318021/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35318021">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2681278523.jpg" alt="������" data-x="1095" data-y="1493">
                
            </div>
            <p>
                

                ������

                
                    <strong>7.7</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30472643/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30472643">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2659301260.jpg" alt="��������4�������ð��" data-x="1400" data-y="2100">
                
            </div>
            <p>
                

                ��������4�������ð��

                
                    <strong>6.1</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34658290/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34658290">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2755684064.jpg" alt="���ľ���" data-x="2025" data-y="3000">
                
            </div>
            <p>
                

                ���ľ���

                
                    <strong>8.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/20276229/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="20276229">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2707553644.jpg" alt="007����Ͼ����" data-x="1691" data-y="2500">
                
            </div>
            <p>
                

                007����Ͼ����

                
                    <strong>6.7</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26933588/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="26933588">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2713726815.jpg" alt="ʥĸ" data-x="2026" data-y="3000">
                
            </div>
            <p>
                

                ʥĸ

                
                    <strong>7.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30409439/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30409439">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2634952893.jpg" alt="��ɽ����" data-x="2000" data-y="2866">
                
            </div>
            <p>
                

                ��ɽ����

                
                    <strong>8.7</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30382416/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30382416">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2675102928.jpg" alt="��Һ2" data-x="1670" data-y="2400">
                
            </div>
            <p>
                

                ��Һ2

                
                    <strong>5.0</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35158375/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35158375">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2686474863.jpg" alt="���Ȱ�" data-x="1130" data-y="1600">
                
            </div>
            <p>
                

                ���Ȱ�

                
                    <strong>8.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35134764/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35134764">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2688141684.jpg" alt="�ϵ�֮��" data-x="2000" data-y="2963">
                
            </div>
            <p>
                

                �ϵ�֮��

                
                    <strong>7.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34865507/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="34865507">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2640615589.jpg" alt="С����" data-x="2000" data-y="3000">
                
            </div>
            <p>
                

                С����

                
                    <strong>7.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34927643/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34927643">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2702495844.jpg" alt="���ų���" data-x="1400" data-y="2059">
                
            </div>
            <p>
                

                ���ų���

                
                    <strong>7.7</strong>
                
            </p>
        </a><a class="item" target="_blank" href="https://movie.douban.com/subject/34970325/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34970325">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2669238453.jpg" alt="�޹���" data-x="1382" data-y="2048">
                
            </div>
            <p>
                

                �޹���

                
                    <strong>7.1</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35240917/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35240917">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2696233262.jpg" alt="Ľ��ڣ�ս����Ե" data-x="2000" data-y="2963">
                
            </div>
            <p>
                

                Ľ��ڣ�ս����Ե

                
                    <strong>7.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/25828589/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="25828589">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2665872718.jpg" alt="�ڹѸ�" data-x="864" data-y="1280">
                
            </div>
            <p>
                

                �ڹѸ�

                
                    <strong>6.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30337388/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="30337388">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2677520025.jpg" alt="ʧ�����" data-x="1080" data-y="1600">
                
            </div>
            <p>
                

                ʧ�����

                
                    <strong>7.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26741632/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="26741632">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2637084112.jpg" alt="X��ǲ�ӣ�ȫԱ����" data-x="2765" data-y="4096">
                
            </div>
            <p>
                

                X��ǲ�ӣ�ȫԱ����

                
                    <strong>8.0</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34869121/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34869121">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2731403566.jpg" alt="����֮Ѫ" data-x="1200" data-y="1710">
                
            </div>
            <p>
                

                ����֮Ѫ

                
                    <strong>6.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34841067/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="34841067">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2629056068.jpg" alt="��ã����Ӣ" data-x="3000" data-y="4292">
                
            </div>
            <p>
                

                ��ã����Ӣ

                
                    <strong>7.7</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35262731/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35262731">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2675919720.jpg" alt="ǳ��С��" data-x="750" data-y="1111">
                
            </div>
            <p>
                

                ǳ��С��

                
                    <strong>8.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/32493124/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="32493124">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2641614433.jpg" alt="����֮��" data-x="5315" data-y="7440">
                
            </div>
            <p>
                

                ����֮��

                
                    <strong>7.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/27124695/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="27124695">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2706359781.jpg" alt="�ǳ�" data-x="1135" data-y="1585">
                
            </div>
            <p>
                

                �ǳ�

                
                    <strong>7.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/33386178/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="33386178">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2722980045.jpg" alt="��˰׵ı���" data-x="2025" data-y="3000">
                
            </div>
            <p>
                

                ��˰׵ı���

                
                    <strong>7.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26838236/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="26838236">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2685536675.jpg" alt="���ܸ�����" data-x="1349" data-y="2000">
                
            </div>
            <p>
                

                ���ܸ�����

                
                    <strong>6.1</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/33457594/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="33457594">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2695961421.jpg" alt="Ħ�ӵ�ɳ" data-x="1187" data-y="1701">
                
            </div>
            <p>
                

                Ħ�ӵ�ɳ

                
                    <strong>8.1</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30344474/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30344474">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2807771124.jpg" alt="������Ů��" data-x="1120" data-y="1590">
                
            </div>
            <p>
                

                ������Ů��

                
                    <strong>7.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34927916/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="34927916">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2687924214.jpg" alt="��������" data-x="2000" data-y="3006">
                
            </div>
            <p>
                

                ��������

                
                    <strong>6.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30137576/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30137576">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2666266209.jpg" alt="����" data-x="629" data-y="900">
                
            </div>
            <p>
                

                ����

                
                    <strong>7.7</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35205446/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35205446">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2684720964.jpg" alt="����Ӣ��" data-x="4000" data-y="5600">
                
            </div>
            <p>
                

                ����Ӣ��

                
                    <strong>5.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/33437580/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="33437580">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2681332523.jpg" alt="������" data-x="770" data-y="1100">
                
            </div>
            <p>
                

                ������

                
                    <strong>7.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35076714/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35076714">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2634360594.jpg" alt="���ˡ�ʩ�ε°���������" data-x="2025" data-y="3000">
                
            </div>
            <p>
                

                ���ˡ�ʩ�ε°���������

                
                    <strong>8.1</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35123985/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35123985">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2678060278.jpg" alt="ƽ��ĸ��" data-x="1434" data-y="2048">
                
            </div>
            <p>
                

                ƽ��ĸ��

                
                    <strong>7.2</strong>
                
            </p>
        </a><a class="item" target="_blank" href="https://movie.douban.com/subject/34852249/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34852249">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2665017565.jpg" alt="ɱ�����ƻ�" data-x="1455" data-y="2048">
                
            </div>
            <p>
                

                ɱ�����ƻ�

                
                    <strong>6.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/33447864/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="33447864">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2766683184.jpg" alt="���" data-x="1124" data-y="1681">
                
            </div>
            <p>
                

                ���

                
                    <strong>6.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30447440/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30447440">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2704450439.jpg" alt="Soho������ҹ" data-x="2126" data-y="3150">
                
            </div>
            <p>
                

                Soho������ҹ

                
                    <strong>6.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/33404512/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="33404512">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2627312853.jpg" alt="��������Ů��" data-x="2891" data-y="4096">
                
            </div>
            <p>
                

                ��������Ů��

                
                    <strong>7.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35101435/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35101435">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2678164205.jpg" alt="˹����" data-x="2001" data-y="2937">
                
            </div>
            <p>
                

                ˹����

                
                    <strong>6.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/33407124/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="33407124">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2641350668.jpg" alt="�˿ͽ��� ������ ׷��ƪ" data-x="1000" data-y="1416">
                
            </div>
            <p>
                

                �˿ͽ��� ������ ׷��ƪ

                
                    <strong>8.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30143331/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30143331">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2702918768.jpg" alt="��ɫͨ����" data-x="1500" data-y="2222">
                
            </div>
            <p>
                

                ��ɫͨ����

                
                    <strong>6.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34966906/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34966906">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2706304062.jpg" alt="һ��Ӣ��" data-x="1944" data-y="2880">
                
            </div>
            <p>
                

                һ��Ӣ��

                
                    <strong>7.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30394797/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30394797">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2674321872.jpg" alt="������ʮ������" data-x="1688" data-y="2500">
                
            </div>
            <p>
                

                ������ʮ������

                
                    <strong>6.1</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/27619748/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="27619748">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2622388983.jpg" alt="���˽�̽��3" data-x="2143" data-y="3000">
                
            </div>
            <p>
                

                ���˽�̽��3

                
                    <strong>5.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/1428581/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="1428581">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2700138245.jpg" alt="������̷" data-x="3481" data-y="4921">
                
            </div>
            <p>
                

                ������̷

                
                    <strong>9.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26140265/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="26140265">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2692391480.jpg" alt="������Σ��" data-x="1349" data-y="2000">
                
            </div>
            <p>
                

                ������Σ��

                
                    <strong>4.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35030151/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35030151">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2682685788.jpg" alt="�����ˮ������" data-x="2126" data-y="2976">
                
            </div>
            <p>
                

                �����ˮ������

                
                    <strong>7.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/25909236/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="25909236">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2672792129.jpg" alt="������Ӧ" data-x="1200" data-y="1778">
                
            </div>
            <p>
                

                ������Ӧ

                
                    <strong>6.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34963486/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34963486">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2635592713.jpg" alt="��Ӱ֮��" data-x="707" data-y="1000">
                
            </div>
            <p>
                

                ��Ӱ֮��

                
                    <strong>7.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/25881778/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="25881778">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2641399262.jpg" alt="��Ҫ������һ��" data-x="1080" data-y="1512">
                
            </div>
            <p>
                

                ��Ҫ������һ��

                
                    <strong>6.0</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34820925/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34820925">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2663190044.jpg" alt="��" data-x="1938" data-y="2880">
                
            </div>
            <p>
                

                ��

                
                    <strong>6.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/3692602/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="3692602">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2710065784.jpg" alt="�����溽" data-x="4000" data-y="5922">
                
            </div>
            <p>
                

                �����溽

                
                    <strong>6.1</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34981939/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34981939">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2681328483.jpg" alt="͵����" data-x="1500" data-y="2222">
                
            </div>
            <p>
                

                ͵����

                
                    <strong>6.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35158124/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35158124">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2673420377.jpg" alt="ʢ��δ��" data-x="1500" data-y="2175">
                
            </div>
            <p>
                

                ʢ��δ��

                
                    <strong>7.1</strong>
                
            </p>
        </a><a class="item" target="_blank" href="https://movie.douban.com/subject/34840705/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34840705">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2687136996.jpg" alt="��������" data-x="4050" data-y="6000">
                
            </div>
            <p>
                

                ��������

                
                    <strong>7.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30465538/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30465538">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2655000580.jpg" alt="������" data-x="2740" data-y="3732">
                
            </div>
            <p>
                

                ������

                
                    <strong>6.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35293160/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35293160">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2690943591.jpg" alt="������������" data-x="1000" data-y="1423">
                
            </div>
            <p>
                

                ������������

                
                    <strong>7.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/27008393/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="27008393">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2719097587.jpg" alt="��������" data-x="5906" data-y="8268">
                
            </div>
            <p>
                

                ��������

                
                    <strong>6.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35669441/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35669441">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2799276725.jpg" alt="ϣ������ɽ��֮��" data-x="1360" data-y="2040">
                
            </div>
            <p>
                

                ϣ������ɽ��֮��

                
                    <strong>8.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34881718/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34881718">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2707727239.jpg" alt="������ˡ" data-x="1500" data-y="2222">
                
            </div>
            <p>
                

                ������ˡ

                
                    <strong>7.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35087699/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35087699">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2666591984.jpg" alt="�й�ҽ��" data-x="2126" data-y="2976">
                
            </div>
            <p>
                

                �й�ҽ��

                
                    <strong>6.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35299584/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35299584">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2680494037.jpg" alt="������˹��" data-x="1013" data-y="1500">
                
            </div>
            <p>
                

                ������˹��

                
                    <strong>6.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30167974/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="30167974">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2627551613.jpg" alt="�˿ͽ��� ������ ����ƪ" data-x="2024" data-y="2866">
                
            </div>
            <p>
                

                �˿ͽ��� ������ ����ƪ

                
                    <strong>7.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30481476/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30481476">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2690707256.jpg" alt="��������" data-x="1500" data-y="2223">
                
            </div>
            <p>
                

                ��������

                
                    <strong>7.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/10428501/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="10428501">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2629054917.jpg" alt="�¡�����սʿ�糡�棺��" data-x="1852" data-y="2621">
                
            </div>
            <p>
                

                �¡�����սʿ�糡�棺��

                
                    <strong>9.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34663377/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34663377">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2734449506.jpg" alt="·��˹��Τ���ļ�������" data-x="4051" data-y="6000">
                
            </div>
            <p>
                

                ·��˹��Τ���ļ�������

                
                    <strong>7.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35196097/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35196097">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2684251260.jpg" alt="���������һ��" data-x="1750" data-y="2500">
                
            </div>
            <p>
                

                ���������һ��

                
                    <strong>6.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35311473/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35311473">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2657020716.jpg" alt="����֮Ѫ2" data-x="750" data-y="1063">
                
            </div>
            <p>
                

                ����֮Ѫ2

                
                    <strong>7.0</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30435124/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="30435124">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2655030796.jpg" alt="����2�����߽���" data-x="1879" data-y="3000">
                
            </div>
            <p>
                

                ����2�����߽���

                
                    <strong>6.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35242942/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35242942">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2638021971.jpg" alt="��ù�԰��������Ƭ" data-x="1313" data-y="1875">
                
            </div>
            <p>
                

                ��ù�԰��������Ƭ

                
                    <strong>7.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26935283/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="26935283">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2629260713.jpg" alt="������" data-x="3571" data-y="4990">
                
            </div>
            <p>
                

                ������

                
                    <strong>5.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35287558/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35287558">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2642244414.jpg" alt="�д𰸵�����" data-x="1841" data-y="2560">
                
            </div>
            <p>
                

                �д𰸵�����

                
                    <strong>7.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35208823/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35208823">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2661923862.jpg" alt="��ý" data-x="1500" data-y="2149">
                
            </div>
            <p>
                

                ��ý

                
                    <strong>6.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30279836/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="30279836">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2637603645.jpg" alt="��ʮһ��" data-x="2000" data-y="2800">
                
            </div>
            <p>
                

                ��ʮһ��

                
                    <strong>7.2</strong>
                
            </p>
        </a><a class="item" target="_blank" href="https://movie.douban.com/subject/35465742/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35465742">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2681045224.jpg" alt="������ǰ" data-x="1200" data-y="1710">
                
            </div>
            <p>
                

                ������ǰ

                
                    <strong>7.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30469922/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30469922">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2729074424.jpg" alt="��������2" data-x="2000" data-y="2962">
                
            </div>
            <p>
                

                ��������2

                
                    <strong>6.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35017064/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35017064">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2652833060.jpg" alt="��ȥ" data-x="3158" data-y="5000">
                
            </div>
            <p>
                

                ��ȥ

                
                    <strong>6.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35231370/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35231370">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2680735532.jpg" alt="�屬" data-x="1000" data-y="1397">
                
            </div>
            <p>
                

                �屬

                
                    <strong>6.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35280911/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35280911">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2633773335.jpg" alt="��ɫ" data-x="2898" data-y="4096">
                
            </div>
            <p>
                

                ��ɫ

                
                    <strong>6.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30174085/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="30174085">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2673412189.jpg" alt="ŭ���ذ�" data-x="1429" data-y="2000">
                
            </div>
            <p>
                

                ŭ���ذ�

                
                    <strong>7.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34880302/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="34880302">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2632862664.jpg" alt="�˳���ӿ" data-x="1429" data-y="2000">
                
            </div>
            <p>
                

                �˳���ӿ

                
                    <strong>6.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26826330/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="26826330">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2628440875.jpg" alt="��ɱС˵��" data-x="780" data-y="1196">
                
            </div>
            <p>
                

                ��ɱС˵��

                
                    <strong>6.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35691909/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="true" data-id="35691909">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2770879108.jpg" alt="����֮�� ǳ��ƪ" data-x="825" data-y="1180">
                
            </div>
            <p>
                
                    <span class="green">
                        <img src="https://img3.doubanio.com/f/movie/caa8f80abecee1fc6f9d31924cef8dd9a24c7227/pics/movie/ic_new.png" width="16" class="new">
                    </span>
                

                ����֮�� ǳ��ƪ

                
                    <strong>8.7</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35477218/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35477218">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2670777611.jpg" alt="����լ" data-x="1500" data-y="2138">
                
            </div>
            <p>
                

                ����լ

                
                    <strong>6.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26703121/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="26703121">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2653946775.jpg" alt="�ڰ�ħŮ������" data-x="6759" data-y="10160">
                
            </div>
            <p>
                

                �ڰ�ħŮ������

                
                    <strong>6.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35161768/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35161768">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2675958609.jpg" alt="����������" data-x="1080" data-y="1542">
                
            </div>
            <p>
                

                ����������

                
                    <strong>7.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35547169/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35547169">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2699152497.jpg" alt="˽�˻�Į" data-x="1170" data-y="1716">
                
            </div>
            <p>
                

                ˽�˻�Į

                
                    <strong>7.1</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/25728006/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="25728006">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2640611704.jpg" alt="�ٶ��뼤��9" data-x="1080" data-y="1596">
                
            </div>
            <p>
                

                �ٶ��뼤��9

                
                    <strong>5.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35158160/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35158160">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2630463690.jpg" alt="�ҵĽ��" data-x="5000" data-y="7478">
                
            </div>
            <p>
                

                �ҵĽ��

                
                    <strong>6.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35651911/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35651911">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2727626416.jpg" alt="����֮�� ���ݷ�ƪ" data-x="708" data-y="1000">
                
            </div>
            <p>
                

                ����֮�� ���ݷ�ƪ

                
                    <strong>8.7</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34888057/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34888057">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2687662638.jpg" alt="�ʲ�����" data-x="4320" data-y="6400">
                
            </div>
            <p>
                

                �ʲ�����

                
                    <strong>7.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35251025/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35251025">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2690743436.jpg" alt="��ɫ���" data-x="1382" data-y="2047">
                
            </div>
            <p>
                

                ��ɫ���

                
                    <strong>7.0</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35225859/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35225859">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2677331311.jpg" alt="С����" data-x="1500" data-y="2222">
                
            </div>
            <p>
                

                С����

                
                    <strong>7.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35259430/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35259430">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2675838753.jpg" alt="���Ƕ��޷���Ϊ����" data-x="750" data-y="1059">
                
            </div>
            <p>
                

                ���Ƕ��޷���Ϊ����

                
                    <strong>7.5</strong>
                
            </p>
        </a><a class="item" target="_blank" href="https://movie.douban.com/subject/35198827/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35198827">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2656407373.jpg" alt="����������ʱ" data-x="1400" data-y="2100">
                
            </div>
            <p>
                

                ����������ʱ

                
                    <strong>6.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30453797/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30453797">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2633279574.jpg" alt="ԡ����" data-x="1000" data-y="1404">
                
            </div>
            <p>
                

                ԡ����

                
                    <strong>7.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35573989/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35573989">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2678028129.jpg" alt="���" data-x="1356" data-y="1929">
                
            </div>
            <p>
                

                ���

                
                    <strong>6.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34804147/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="34804147">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2628052135.jpg" alt="Ѱ����˵" data-x="2765" data-y="4096">
                
            </div>
            <p>
                

                Ѱ����˵

                
                    <strong>7.0</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/27605563/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="27605563">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2587966857.jpg" alt="¹��" data-x="1334" data-y="2000">
                
            </div>
            <p>
                

                ¹��

                
                    <strong>5.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35202365/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35202365">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2685374824.jpg" alt="���������" data-x="1131" data-y="1600">
                
            </div>
            <p>
                

                ���������

                
                    <strong>7.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35374186/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="true" data-id="35374186">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2652013893.jpg" alt="�Ļ��˷�" data-x="750" data-y="1059">
                
            </div>
            <p>
                
                    <span class="green">
                        <img src="https://img3.doubanio.com/f/movie/caa8f80abecee1fc6f9d31924cef8dd9a24c7227/pics/movie/ic_new.png" width="16" class="new">
                    </span>
                

                �Ļ��˷�

                
                    <strong>6.1</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35195869/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="true" data-id="35195869">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2854783787.jpg" alt="�������" data-x="2025" data-y="3000">
                
            </div>
            <p>
                
                    <span class="green">
                        <img src="https://img3.doubanio.com/f/movie/caa8f80abecee1fc6f9d31924cef8dd9a24c7227/pics/movie/ic_new.png" width="16" class="new">
                    </span>
                

                �������

                
                    <strong>6.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30378158/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="30378158">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2629408730.jpg" alt="���ܷÿ�" data-x="6213" data-y="9047">
                
            </div>
            <p>
                

                ���ܷÿ�

                
                    <strong>5.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/33454993/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="33454993">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2638968571.jpg" alt="����̽���ϣ��ɫ���ӵ�" data-x="7785" data-y="10721">
                
            </div>
            <p>
                

                ����̽���ϣ��ɫ���ӵ�

                
                    <strong>5.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/27594653/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="27594653">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2632091530.jpg" alt="�����ռ�" data-x="1656" data-y="2500">
                
            </div>
            <p>
                

                �����ռ�

                
                    <strong>5.7</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30176790/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30176790">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2706812406.jpg" alt="÷�޷�" data-x="1500" data-y="2140">
                
            </div>
            <p>
                

                ÷�޷�

                
                    <strong>6.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/6874475/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="6874475">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2676934276.jpg" alt="��������" data-x="2000" data-y="3012">
                
            </div>
            <p>
                

                ��������

                
                    <strong>5.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26856202/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="26856202">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2654489281.jpg" alt="������" data-x="3484" data-y="4724">
                
            </div>
            <p>
                

                ������

                
                    <strong>6.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34779692/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="34779692">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2631711326.jpg" alt="�������߸����" data-x="4370" data-y="6201">
                
            </div>
            <p>
                

                �������߸����

                
                    <strong>6.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30229667/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30229667">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2637896820.jpg" alt="���ܴ󷴹�" data-x="1500" data-y="2222">
                
            </div>
            <p>
                

                ���ܴ󷴹�

                
                    <strong>7.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/27200859/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="27200859">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2678455893.jpg" alt="����Զ��" data-x="1780" data-y="2670">
                
            </div>
            <p>
                

                ����Զ��

                
                    <strong>9.1</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/33447881/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="33447881">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2666471566.jpg" alt="�˵��޷������" data-x="2000" data-y="2941">
                
            </div>
            <p>
                

                �˵��޷������

                
                    <strong>7.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30206311/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="30206311">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2651298629.jpg" alt="�ž�֮��2" data-x="3957" data-y="5793">
                
            </div>
            <p>
                

                �ž�֮��2

                
                    <strong>6.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/27077479/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="27077479">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2641811991.jpg" alt="�л�3" data-x="2764" data-y="4096">
                
            </div>
            <p>
                

                �л�3

                
                    <strong>6.4</strong>
                
            </p>
        </a><a class="item" target="_blank" href="https://movie.douban.com/subject/33450810/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="33450810">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2687175435.jpg" alt="����" data-x="1170" data-y="1671">
                
            </div>
            <p>
                

                ����

                
                    <strong>5.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/29984000/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="29984000">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2654729576.jpg" alt="�ȴ�����" data-x="1000" data-y="1414">
                
            </div>
            <p>
                

                �ȴ�����

                
                    <strong>6.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35685660/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35685660">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2804529364.jpg" alt="2021ȥ��" data-x="960" data-y="1350">
                
            </div>
            <p>
                

                2021ȥ��

                
                    <strong>6.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35288767/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35288767">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2666303410.jpg" alt="������" data-x="2000" data-y="2789">
                
            </div>
            <p>
                

                ������

                
                    <strong>7.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26604217/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="26604217">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2732133934.jpg" alt="�￨��һ��" data-x="2700" data-y="4000">
                
            </div>
            <p>
                

                �￨��һ��

                
                    <strong>6.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35151297/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35151297">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2669957808.jpg" alt="�����������İ���" data-x="1200" data-y="1777">
                
            </div>
            <p>
                

                �����������İ���

                
                    <strong>7.0</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35310153/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35310153">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2633604200.jpg" alt="����2" data-x="579" data-y="873">
                
            </div>
            <p>
                

                ����2

                
                    <strong>7.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35287908/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35287908">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2672428635.jpg" alt="����ȸ�߹���" data-x="1446" data-y="2048">
                
            </div>
            <p>
                

                ����ȸ�߹���

                
                    <strong>6.1</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34614665/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34614665">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2654990612.jpg" alt="��ˮ��" data-x="1013" data-y="1500">
                
            </div>
            <p>
                

                ��ˮ��

                
                    <strong>7.1</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/27046740/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="27046740">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2642842673.jpg" alt="��֮ŭ" data-x="2765" data-y="4096">
                
            </div>
            <p>
                

                ��֮ŭ

                
                    <strong>6.7</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30459571/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="30459571">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2678875868.jpg" alt="����֮ս" data-x="1701" data-y="2721">
                
            </div>
            <p>
                

                ����֮ս

                
                    <strong>5.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/33973077/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="33973077">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2680748636.jpg" alt="ƤƤ³��³����֮��ͷС��" data-x="3543" data-y="4961">
                
            </div>
            <p>
                

                ƤƤ³��³����֮��ͷС��

                
                    <strong>6.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34908189/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="34908189">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2649579601.jpg" alt="���Ѽ��ؾ��ؼ�" data-x="2025" data-y="3000">
                
            </div>
            <p>
                

                ���Ѽ��ؾ��ؼ�

                
                    <strong>9.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30351365/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30351365">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2681381987.jpg" alt="����¥��" data-x="1417" data-y="1925">
                
            </div>
            <p>
                

                ����¥��

                
                    <strong>6.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34809114/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="34809114">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2588141278.jpg" alt="����ѵ��Ӫ" data-x="2025" data-y="3000">
                
            </div>
            <p>
                

                ����ѵ��Ӫ

                
                    <strong>6.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/32568661/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="32568661">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2676932860.jpg" alt="���������С��" data-x="1819" data-y="2547">
                
            </div>
            <p>
                

                ���������С��

                
                    <strong>6.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35236759/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35236759">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2669093839.jpg" alt="��ʤŮ��" data-x="1939" data-y="2880">
                
            </div>
            <p>
                

                ��ʤŮ��

                
                    <strong>6.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35093796/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35093796">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2677276852.jpg" alt="�漣" data-x="1979" data-y="2835">
                
            </div>
            <p>
                

                �漣

                
                    <strong>7.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26613692/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="26613692">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2634253484.jpg" alt="��˹����ս���" data-x="2764" data-y="4096">
                
            </div>
            <p>
                

                ��˹����ս���

                
                    <strong>6.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35210620/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35210620">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2672676397.jpg" alt="������˹����" data-x="1200" data-y="1600">
                
            </div>
            <p>
                

                ������˹����

                
                    <strong>7.6</strong>
                
            </p>
        </a><a class="item" target="_blank" href="https://movie.douban.com/subject/35245762/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35245762">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2704531912.jpg" alt="��͵����" data-x="1500" data-y="2222">
                
            </div>
            <p>
                

                ��͵����

                
                    <strong>6.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/27056396/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="27056396">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2651996671.jpg" alt="�����ϰ�2" data-x="1293" data-y="2047">
                
            </div>
            <p>
                

                �����ϰ�2

                
                    <strong>6.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/32493666/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="32493666">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2640758773.jpg" alt="׷������" data-x="4858" data-y="6802">
                
            </div>
            <p>
                

                ׷������

                
                    <strong>5.0</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34973557/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34973557">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2641605963.jpg" alt="����������" data-x="2898" data-y="4096">
                
            </div>
            <p>
                

                ����������

                
                    <strong>6.7</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30372022/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30372022">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2659155163.jpg" alt="������ʿ" data-x="1944" data-y="2880">
                
            </div>
            <p>
                

                ������ʿ

                
                    <strong>6.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30213339/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="30213339">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2656009080.jpg" alt="�ȵ���2�����ܼƻ�" data-x="540" data-y="800">
                
            </div>
            <p>
                

                �ȵ���2�����ܼƻ�

                
                    <strong>7.0</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30216729/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30216729">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2647131304.jpg" alt="���Ʊ���2" data-x="4320" data-y="6660">
                
            </div>
            <p>
                

                ���Ʊ���2

                
                    <strong>6.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35221424/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35221424">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2681647789.jpg" alt="֮��3" data-x="809" data-y="1200">
                
            </div>
            <p>
                

                ֮��3

                
                    <strong>5.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/33450426/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="33450426">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2637809736.jpg" alt="��⾪��9������" data-x="1946" data-y="3000">
                
            </div>
            <p>
                

                ��⾪��9������

                
                    <strong>5.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26820621/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="26820621">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2762894040.jpg" alt="��������" data-x="2063" data-y="3000">
                
            </div>
            <p>
                

                ��������

                
                    <strong>6.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35125443/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35125443">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2665014115.jpg" alt="1921" data-x="5379" data-y="7530">
                
            </div>
            <p>
                

                1921

                
                    <strong>6.7</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/23774832/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="23774832">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2665927388.jpg" alt="��칷���︥" data-x="961" data-y="1500">
                
            </div>
            <p>
                

                ��칷���︥

                
                    <strong>6.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35184151/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35184151">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2626807774.jpg" alt="ɱ��Ԣ�� �ڶ���" data-x="2894" data-y="4096">
                
            </div>
            <p>
                

                ɱ��Ԣ�� �ڶ���

                
                    <strong>7.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30444940/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30444940">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2671039153.jpg" alt="�־��3" data-x="1500" data-y="2222">
                
            </div>
            <p>
                

                �־��3

                
                    <strong>7.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34857667/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34857667">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2668580982.jpg" alt="�ǵ�˹һ��2" data-x="1080" data-y="1600">
                
            </div>
            <p>
                

                �ǵ�˹һ��2

                
                    <strong>6.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35441797/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35441797">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2812277441.jpg" alt="�������" data-x="1430" data-y="2048">
                
            </div>
            <p>
                

                �������

                
                    <strong>6.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34856590/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34856590">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2670915379.jpg" alt="��ɫ����" data-x="1046" data-y="1500">
                
            </div>
            <p>
                

                ��ɫ����

                
                    <strong>7.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30180126/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30180126">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2639263452.jpg" alt="�����Ů��" data-x="1500" data-y="2222">
                
            </div>
            <p>
                

                �����Ů��

                
                    <strong>6.1</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35283045/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35283045">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2734120983.jpg" alt="����ư�" data-x="2000" data-y="3000">
                
            </div>
            <p>
                

                ����ư�

                
                    <strong>6.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26915921/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="26915921">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2675211748.jpg" alt="��ס����2" data-x="2763" data-y="4096">
                
            </div>
            <p>
                

                ��ס����2

                
                    <strong>6.5</strong>
                
            </p>
        </a><a class="item" target="_blank" href="https://movie.douban.com/subject/30201133/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="30201133">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2654612159.jpg" alt="����սʿ�ߴ� ����Ĺ���ά" data-x="1024" data-y="1445">
                
            </div>
            <p>
                

                ����սʿ�ߴ� ����Ĺ���ά

                
                    <strong>8.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34960130/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34960130">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2583403599.jpg" alt="��լ" data-x="720" data-y="960">
                
            </div>
            <p>
                

                ��լ

                
                    <strong>5.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35360295/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35360295">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2652590749.jpg" alt="����" data-x="1400" data-y="1995">
                
            </div>
            <p>
                

                ����

                
                    <strong>6.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35190036/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="true" data-id="35190036">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2678142009.jpg" alt="һ��˳��" data-x="2740" data-y="3732">
                
            </div>
            <p>
                
                    <span class="green">
                        <img src="https://img3.doubanio.com/f/movie/caa8f80abecee1fc6f9d31924cef8dd9a24c7227/pics/movie/ic_new.png" width="16" class="new">
                    </span>
                

                һ��˳��

                
                    <strong>7.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35259282/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35259282">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2687792757.jpg" alt="Ԯ��" data-x="1060" data-y="1500">
                
            </div>
            <p>
                

                Ԯ��

                
                    <strong>7.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26615748/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="26615748">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2654959196.jpg" alt="׷���Ծ�" data-x="729" data-y="1080">
                
            </div>
            <p>
                

                ׷���Ծ�

                
                    <strong>6.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35204897/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35204897">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2636638694.jpg" alt="���������մ�" data-x="750" data-y="1056">
                
            </div>
            <p>
                

                ���������մ�

                
                    <strong>5.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35375982/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35375982">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2685482998.jpg" alt="��ά��Ү��" data-x="1200" data-y="1800">
                
            </div>
            <p>
                

                ��ά��Ү��

                
                    <strong>7.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/3439312/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="3439312">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2632043260.jpg" alt="è������" data-x="4000" data-y="5823">
                
            </div>
            <p>
                

                è������

                
                    <strong>5.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30389627/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30389627">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2662756946.jpg" alt="�ǹ���" data-x="2587" data-y="4096">
                
            </div>
            <p>
                

                �ǹ���

                
                    <strong>5.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35464967/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35464967">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2673396594.jpg" alt="Ӳ��ǹ��" data-x="960" data-y="1440">
                
            </div>
            <p>
                

                Ӳ��ǹ��

                
                    <strong>7.0</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35115642/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35115642">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2692942421.jpg" alt="ƽ��ɭ��" data-x="3508" data-y="4961">
                
            </div>
            <p>
                

                ƽ��ɭ��

                
                    <strong>6.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35116325/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35116325">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2691401250.jpg" alt="����¼���94" data-x="1000" data-y="1500">
                
            </div>
            <p>
                

                ����¼���94

                
                    <strong>6.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/27177908/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="27177908">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2675197481.jpg" alt="����" data-x="1500" data-y="2222">
                
            </div>
            <p>
                

                ����

                
                    <strong>6.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35271841/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35271841">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2742358006.jpg" alt="������ķ" data-x="1984" data-y="2835">
                
            </div>
            <p>
                

                ������ķ

                
                    <strong>6.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35442458/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35442458">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2678672493.jpg" alt="�Ϻ���" data-x="455" data-y="674">
                
            </div>
            <p>
                

                �Ϻ���

                
                    <strong>7.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35164328/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35164328">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2634025511.jpg" alt="ɨ�ڡ���ս" data-x="1435" data-y="2200">
                
            </div>
            <p>
                

                ɨ�ڡ���ս

                
                    <strong>6.0</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30422485/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30422485">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2656934367.jpg" alt="����" data-x="1187" data-y="1701">
                
            </div>
            <p>
                

                ����

                
                    <strong>6.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/3099221/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="3099221">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2643872011.jpg" alt="�����˾���" data-x="1500" data-y="2222">
                
            </div>
            <p>
                

                �����˾���

                
                    <strong>5.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26935358/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="26935358">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2709871678.jpg" alt="���ܵ���������" data-x="1080" data-y="1536">
                
            </div>
            <p>
                

                ���ܵ���������

                
                    <strong>6.6</strong>
                
            </p>
        </a><a class="item" target="_blank" href="https://movie.douban.com/subject/35419225/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35419225">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2707359633.jpg" alt="������֮��" data-x="1070" data-y="1500">
                
            </div>
            <p>
                

                ������֮��

                
                    <strong>7.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34873745/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34873745">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2676919475.jpg" alt="������" data-x="2025" data-y="3000">
                
            </div>
            <p>
                

                ������

                
                    <strong>6.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26867808/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="26867808">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2685656324.jpg" alt="��������" data-x="2766" data-y="4096">
                
            </div>
            <p>
                

                ��������

                
                    <strong>6.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35128768/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35128768">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2612400333.jpg" alt="ϣ����櫵���ʿ ��֯��������" data-x="700" data-y="990">
                
            </div>
            <p>
                

                ϣ����櫵���ʿ ��֯��������

                
                    <strong>8.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35516745/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35516745">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2674392637.jpg" alt="����" data-x="1276" data-y="1884">
                
            </div>
            <p>
                

                ����

                
                    <strong>7.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/33440550/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="33440550">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2672784917.jpg" alt="���ס��Ƶ��۾�" data-x="1334" data-y="2000">
                
            </div>
            <p>
                

                ���ס��Ƶ��۾�

                
                    <strong>6.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/27179288/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="27179288">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2665626425.jpg" alt="Ѫɫ���" data-x="729" data-y="1080">
                
            </div>
            <p>
                

                Ѫɫ���

                
                    <strong>6.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/1431694/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="1431694">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2693881679.jpg" alt="�������ŵĵ粨" data-x="2160" data-y="3030">
                
            </div>
            <p>
                

                �������ŵĵ粨

                
                    <strong>8.0</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34981336/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34981336">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2784021596.jpg" alt="����" data-x="1000" data-y="1400">
                
            </div>
            <p>
                

                ����

                
                    <strong>7.1</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35384201/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35384201">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2681524736.jpg" alt="��Ȯ������" data-x="1356" data-y="1929">
                
            </div>
            <p>
                

                ��Ȯ������

                
                    <strong>7.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34917447/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="34917447">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2658143548.jpg" alt="��Խ" data-x="1067" data-y="1600">
                
            </div>
            <p>
                

                ��Խ

                
                    <strong>5.0</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35197314/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35197314">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2756608100.jpg" alt="�����" data-x="810" data-y="1200">
                
            </div>
            <p>
                

                �����

                
                    <strong>6.0</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35007363/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35007363">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2648204312.jpg" alt="����/��λָ�� �վ������ ��λʱ�����������" data-x="2899" data-y="4096">
                
            </div>
            <p>
                

                ����/��λָ�� �վ������ ��λʱ�����������

                
                    <strong>6.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35429502/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35429502">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2647464257.jpg" alt="�������������" data-x="2000" data-y="2866">
                
            </div>
            <p>
                

                �������������

                
                    <strong>7.1</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34955909/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34955909">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2675863739.jpg" alt="��ħ�ˣ���֮ج��" data-x="1500" data-y="2222">
                
            </div>
            <p>
                

                ��ħ�ˣ���֮ج��

                
                    <strong>7.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26823520/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="26823520">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2681329662.jpg" alt="�ճ�����ָ��" data-x="4370" data-y="6201">
                
            </div>
            <p>
                

                �ճ�����ָ��

                
                    <strong>4.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30400539/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30400539">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2680985686.jpg" alt="����" data-x="1500" data-y="2222">
                
            </div>
            <p>
                

                ����

                
                    <strong>6.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30464901/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="30464901">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2641910067.jpg" alt="Ѱ����" data-x="655" data-y="950">
                
            </div>
            <p>
                

                Ѱ����

                
                    <strong>6.0</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26949852/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="26949852">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2625736779.jpg" alt="�츣" data-x="1300" data-y="1856">
                
            </div>
            <p>
                

                �츣

                
                    <strong>5.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30391228/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="30391228">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2654767767.jpg" alt="�˲�����ϰ�" data-x="4370" data-y="6201">
                
            </div>
            <p>
                

                �˲�����ϰ�

                
                    <strong>6.5</strong>
                
            </p>
        </a><a class="item" target="_blank" href="https://movie.douban.com/subject/34950968/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34950968">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2648204952.jpg" alt="��Ů���� Revue Starlight �糡��" data-x="566" data-y="800">
                
            </div>
            <p>
                

                ��Ů���� Revue Starlight �糡��

                
                    <strong>8.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35178785/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35178785">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2692328438.jpg" alt="������" data-x="1500" data-y="2222">
                
            </div>
            <p>
                

                ������

                
                    <strong>6.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35584688/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="true" data-id="35584688">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2851355051.jpg" alt="���ĸ�ӡ��" data-x="750" data-y="1164">
                
            </div>
            <p>
                
                    <span class="green">
                        <img src="https://img3.doubanio.com/f/movie/caa8f80abecee1fc6f9d31924cef8dd9a24c7227/pics/movie/ic_new.png" width="16" class="new">
                    </span>
                

                ���ĸ�ӡ��

                
                    <strong>6.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30483429/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="true" data-id="30483429">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2834428418.jpg" alt="��ѧ�о�" data-x="1170" data-y="1718">
                
            </div>
            <p>
                
                    <span class="green">
                        <img src="https://img3.doubanio.com/f/movie/caa8f80abecee1fc6f9d31924cef8dd9a24c7227/pics/movie/ic_new.png" width="16" class="new">
                    </span>
                

                ��ѧ�о�

                
                    <strong>5.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26818326/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="26818326">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2673991933.jpg" alt="���μ�֮��������" data-x="1560" data-y="3000">
                
            </div>
            <p>
                

                ���μ�֮��������

                
                    <strong>5.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/33446375/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="33446375">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2675546699.jpg" alt="����" data-x="2000" data-y="2865">
                
            </div>
            <p>
                

                ����

                
                    <strong>5.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35198690/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35198690">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2627012348.jpg" alt="�糡�� ��ɫС˵��~playback~" data-x="906" data-y="1280">
                
            </div>
            <p>
                

                �糡�� ��ɫС˵��~playback~

                
                    <strong>7.0</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35145064/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35145064">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2674501696.jpg" alt="�������ڴ���" data-x="1700" data-y="2422">
                
            </div>
            <p>
                

                �������ڴ���

                
                    <strong>6.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30037194/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30037194">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2629058776.jpg" alt="�ᰮ��Ӱ���Ӳ�С��" data-x="750" data-y="1065">
                
            </div>
            <p>
                

                �ᰮ��Ӱ���Ӳ�С��

                
                    <strong>7.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/25834936/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="25834936">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2657554193.jpg" alt="���д�������´���" data-x="2764" data-y="4096">
                
            </div>
            <p>
                

                ���д�������´���

                
                    <strong>6.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34852311/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34852311">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2648436850.jpg" alt="��������" data-x="1383" data-y="2048">
                
            </div>
            <p>
                

                ��������

                
                    <strong>6.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35115594/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35115594">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2632095592.jpg" alt="���ܵ�����" data-x="630" data-y="897">
                
            </div>
            <p>
                

                ���ܵ�����

                
                    <strong>5.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35452679/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35452679">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2699933240.jpg" alt="ͯһ������" data-x="4961" data-y="7016">
                
            </div>
            <p>
                

                ͯһ������

                
                    <strong>7.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/10523152/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="10523152">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2675376450.jpg" alt="����������" data-x="2160" data-y="3200">
                
            </div>
            <p>
                

                ����������

                
                    <strong>6.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35390972/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35390972">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2712253103.jpg" alt="ճ��һ��ĸ���" data-x="1481" data-y="2222">
                
            </div>
            <p>
                

                ճ��һ��ĸ���

                
                    <strong>7.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35183025/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35183025">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2722336852.jpg" alt="����ȱϯ������ʷ" data-x="1187" data-y="1701">
                
            </div>
            <p>
                

                ����ȱϯ������ʷ

                
                    <strong>6.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35360566/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35360566">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2686465704.jpg" alt="�������������ʱ����ʲô��" data-x="800" data-y="1185">
                
            </div>
            <p>
                

                �������������ʱ����ʲô��

                
                    <strong>7.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/27089580/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="27089580">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2665617507.jpg" alt="�־��" data-x="1500" data-y="2222">
                
            </div>
            <p>
                

                �־��

                
                    <strong>5.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35009298/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35009298">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2660101405.jpg" alt="��" data-x="1500" data-y="2222">
                
            </div>
            <p>
                

                ��

                
                    <strong>6.0</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35441896/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35441896">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2641806535.jpg" alt="������ʦ" data-x="581" data-y="909">
                
            </div>
            <p>
                

                ������ʦ

                
                    <strong>7.6</strong>
                
            </p>
        </a><a class="item" target="_blank" href="https://movie.douban.com/subject/34945502/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34945502">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2623117831.jpg" alt="�ھ�" data-x="694" data-y="1000">
                
            </div>
            <p>
                

                �ھ�

                
                    <strong>7.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34881663/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34881663">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2661661947.jpg" alt="��ͽ" data-x="4050" data-y="6000">
                
            </div>
            <p>
                

                ��ͽ

                
                    <strong>5.7</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34882845/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34882845">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2621616665.jpg" alt="������Դ" data-x="2740" data-y="3732">
                
            </div>
            <p>
                

                ������Դ

                
                    <strong>5.7</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35522302/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35522302">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2673836120.jpg" alt="�������" data-x="768" data-y="1024">
                
            </div>
            <p>
                

                �������

                
                    <strong>7.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35150248/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35150248">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2723194489.jpg" alt="ԩ���˽ⲻ�˽�" data-x="1704" data-y="2360">
                
            </div>
            <p>
                

                ԩ���˽ⲻ�˽�

                
                    <strong>6.7</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34943349/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34943349">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2667391667.jpg" alt="��Ů�˵����" data-x="729" data-y="1080">
                
            </div>
            <p>
                

                ��Ů�˵����

                
                    <strong>7.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30336307/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="30336307">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2656628179.jpg" alt="ٸ֮��" data-x="2000" data-y="3000">
                
            </div>
            <p>
                

                ٸ֮��

                
                    <strong>5.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/33433405/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="33433405">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2628845704.jpg" alt="���" data-x="1013" data-y="1500">
                
            </div>
            <p>
                

                ���

                
                    <strong>7.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35122773/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35122773">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2628559841.jpg" alt="����ʢ��֮��" data-x="1767" data-y="2500">
                
            </div>
            <p>
                

                ����ʢ��֮��

                
                    <strong>5.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35054837/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35054837">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2619484634.jpg" alt="���������� ���� vs ���� Game of Future" data-x="639" data-y="900">
                
            </div>
            <p>
                

                ���������� ���� vs ���� Game of Future

                
                    <strong>6.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34839344/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="34839344">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2662473840.jpg" alt="�����ܺ���" data-x="3000" data-y="4257">
                
            </div>
            <p>
                

                �����ܺ���

                
                    <strong>4.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30465068/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30465068">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2632592932.jpg" alt="Ů��Ҫ����" data-x="1500" data-y="2222">
                
            </div>
            <p>
                

                Ů��Ҫ����

                
                    <strong>7.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35335784/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35335784">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2631088441.jpg" alt="����̽���ϣ��ɫ�Ĳ��ڳ�֤��" data-x="640" data-y="905">
                
            </div>
            <p>
                

                ����̽���ϣ��ɫ�Ĳ��ڳ�֤��

                
                    <strong>6.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34988584/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="34988584">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2819529042.jpg" alt="ǧ�ﲻ����" data-x="770" data-y="1080">
                
            </div>
            <p>
                

                ǧ�ﲻ����

                
                    <strong>5.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34954053/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34954053">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2628901958.jpg" alt="��û��̸���ǳ�����" data-x="1214" data-y="1734">
                
            </div>
            <p>
                

                ��û��̸���ǳ�����

                
                    <strong>5.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35312401/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35312401">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2732882844.jpg" alt="����" data-x="1433" data-y="2048">
                
            </div>
            <p>
                

                ����

                
                    <strong>7.0</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35463973/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35463973">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2664170473.jpg" alt="��������" data-x="2000" data-y="2866">
                
            </div>
            <p>
                

                ��������

                
                    <strong>5.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35182677/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35182677">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2642827176.jpg" alt="Ȯ����" data-x="750" data-y="1059">
                
            </div>
            <p>
                

                Ȯ����

                
                    <strong>6.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26996524/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="26996524">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2627392971.jpg" alt="760�ŷ���" data-x="1944" data-y="2880">
                
            </div>
            <p>
                

                760�ŷ���

                
                    <strong>7.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30444938/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30444938">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2668347584.jpg" alt="�־��2" data-x="1500" data-y="2222">
                
            </div>
            <p>
                

                �־��2

                
                    <strong>6.5</strong>
                
            </p>
        </a>"""
tree = etree.XML(xml)
result = tree.xpath("")