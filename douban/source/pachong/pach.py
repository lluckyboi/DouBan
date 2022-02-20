from lxml import etree
xml = """
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35144311/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35144311">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2702755317.jpg" alt="雄狮少年" data-x="8268" data-y="11576">
                
            </div>
            <p>
                

                雄狮少年

                
                    <strong>8.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34990918/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="true" data-id="34990918">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2673290266.jpg" alt="空白" data-x="1052" data-y="1499">
                
            </div>
            <p>
                
                    <span class="green">
                        <img src="https://img3.doubanio.com/f/movie/caa8f80abecee1fc6f9d31924cef8dd9a24c7227/pics/movie/ic_new.png" width="16" class="new">
                    </span>
                

                空白

                
                    <strong>7.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35045591/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="true" data-id="35045591">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2808318200.jpg" alt="汪汪队立大功大电影" data-x="672" data-y="1000">
                
            </div>
            <p>
                
                    <span class="green">
                        <img src="https://img3.doubanio.com/f/movie/caa8f80abecee1fc6f9d31924cef8dd9a24c7227/pics/movie/ic_new.png" width="16" class="new">
                    </span>
                

                汪汪队立大功大电影

                
                    <strong>7.1</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35422807/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35422807">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2724443759.jpg" alt="扬名立万" data-x="2088" data-y="3000">
                
            </div>
            <p>
                

                扬名立万

                
                    <strong>7.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/27605105/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="27605105">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2757579107.jpg" alt="玉面情魔" data-x="2765" data-y="4096">
                
            </div>
            <p>
                

                玉面情魔

                
                    <strong>6.7</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/3078409/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="3078409">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2701416129.jpg" alt="古驰家族" data-x="1013" data-y="1500">
                
            </div>
            <p>
                

                古驰家族

                
                    <strong>6.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35242938/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35242938">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2678037153.jpg" alt="瀑布" data-x="1448" data-y="2048">
                
            </div>
            <p>
                

                瀑布

                
                    <strong>7.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35068653/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35068653">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2770857575.jpg" alt="误杀2" data-x="9999" data-y="14004">
                
            </div>
            <p>
                

                误杀2

                
                    <strong>5.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34447553/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34447553">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2669034145.jpg" alt="世界上最糟糕的人" data-x="595" data-y="842">
                
            </div>
            <p>
                

                世界上最糟糕的人

                
                    <strong>7.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35437945/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="true" data-id="35437945">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2641407927.jpg" alt="枕刀歌之尘世行" data-x="1080" data-y="1920">
                
            </div>
            <p>
                
                    <span class="green">
                        <img src="https://img3.doubanio.com/f/movie/caa8f80abecee1fc6f9d31924cef8dd9a24c7227/pics/movie/ic_new.png" width="16" class="new">
                    </span>
                

                枕刀歌之尘世行

                
                    <strong>7.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35235502/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35235502">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2639821491.jpg" alt="驾驶我的车" data-x="2000" data-y="2829">
                
            </div>
            <p>
                

                驾驶我的车

                
                    <strong>8.0</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34884712/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34884712">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2730833093.jpg" alt="不要抬头" data-x="1080" data-y="1920">
                
            </div>
            <p>
                

                不要抬头

                
                    <strong>7.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30300279/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30300279">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2586398074.jpg" alt="法兰西特派" data-x="4048" data-y="6285">
                
            </div>
            <p>
                

                法兰西特派

                
                    <strong>7.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/3001114/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="3001114">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2687443734.jpg" alt="沙丘" data-x="2764" data-y="4096">
                
            </div>
            <p>
                

                沙丘

                
                    <strong>7.7</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35652715/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35652715">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2734251152.jpg" alt="杰伊·比姆" data-x="1000" data-y="1500">
                
            </div>
            <p>
                

                杰伊·比姆

                
                    <strong>8.7</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30223888/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30223888">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2677303737.jpg" alt="永恒族" data-x="1688" data-y="2500">
                
            </div>
            <p>
                

                永恒族

                
                    <strong>5.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/33437152/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="33437152">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2678298618.jpg" alt="犬之力" data-x="1500" data-y="2222">
                
            </div>
            <p>
                

                犬之力

                
                    <strong>7.7</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35258381/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35258381">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2717809625.jpg" alt="天鹅挽歌" data-x="2000" data-y="3000">
                
            </div>
            <p>
                

                天鹅挽歌

                
                    <strong>7.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35294995/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35294995">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2683055011.jpg" alt="我和我的父辈" data-x="2857" data-y="4000">
                
            </div>
            <p>
                

                我和我的父辈

                
                    <strong>6.5</strong>
                
            </p>
        </a><a class="item" target="_blank" href="https://movie.douban.com/subject/35286583/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35286583">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2666651888.jpg" alt="蜡笔小新：谜团！花之天下春日部学院" data-x="1000" data-y="1414">
                
            </div>
            <p>
                

                蜡笔小新：谜团！花之天下春日部学院

                
                    <strong>9.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26962981/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="26962981">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2732782860.jpg" alt="欢乐好声音2" data-x="1012" data-y="1500">
                
            </div>
            <p>
                

                欢乐好声音2

                
                    <strong>7.1</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/25845392/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="25845392">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2681329386.jpg" alt="长津湖" data-x="1080" data-y="1513">
                
            </div>
            <p>
                

                长津湖

                
                    <strong>7.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26897885/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="26897885">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2721066869.jpg" alt="芬奇" data-x="720" data-y="1080">
                
            </div>
            <p>
                

                芬奇

                
                    <strong>8.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35134724/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35134724">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2807936075.jpg" alt="魔法满屋" data-x="3000" data-y="4188">
                
            </div>
            <p>
                

                魔法满屋

                
                    <strong>6.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26996619/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="26996619">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2734316987.jpg" alt="古董局中局" data-x="1785" data-y="2500">
                
            </div>
            <p>
                

                古董局中局

                
                    <strong>5.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34801038/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34801038">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2844387600.jpg" alt="黑客帝国：矩阵重启" data-x="4000" data-y="5929">
                
            </div>
            <p>
                

                黑客帝国：矩阵重启

                
                    <strong>5.7</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30279170/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30279170">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2690712224.jpg" alt="倒数时刻" data-x="1500" data-y="2222">
                
            </div>
            <p>
                

                倒数时刻

                
                    <strong>8.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35360296/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35360296">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2687984714.jpg" alt="偶然与想象" data-x="1460" data-y="2064">
                
            </div>
            <p>
                

                偶然与想象

                
                    <strong>8.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35318021/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35318021">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2681278523.jpg" alt="正发生" data-x="1095" data-y="1493">
                
            </div>
            <p>
                

                正发生

                
                    <strong>7.7</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30472643/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30472643">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2659301260.jpg" alt="精灵旅社4：变身大冒险" data-x="1400" data-y="2100">
                
            </div>
            <p>
                

                精灵旅社4：变身大冒险

                
                    <strong>6.1</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34658290/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34658290">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2755684064.jpg" alt="最后的决斗" data-x="2025" data-y="3000">
                
            </div>
            <p>
                

                最后的决斗

                
                    <strong>8.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/20276229/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="20276229">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2707553644.jpg" alt="007：无暇赴死" data-x="1691" data-y="2500">
                
            </div>
            <p>
                

                007：无暇赴死

                
                    <strong>6.7</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26933588/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="26933588">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2713726815.jpg" alt="圣母" data-x="2026" data-y="3000">
                
            </div>
            <p>
                

                圣母

                
                    <strong>7.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30409439/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30409439">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2634952893.jpg" alt="兹山鱼谱" data-x="2000" data-y="2866">
                
            </div>
            <p>
                

                兹山鱼谱

                
                    <strong>8.7</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30382416/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30382416">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2675102928.jpg" alt="毒液2" data-x="1670" data-y="2400">
                
            </div>
            <p>
                

                毒液2

                
                    <strong>5.0</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35158375/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35158375">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2686474863.jpg" alt="法比安" data-x="1130" data-y="1600">
                
            </div>
            <p>
                

                法比安

                
                    <strong>8.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35134764/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35134764">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2688141684.jpg" alt="上帝之手" data-x="2000" data-y="2963">
                
            </div>
            <p>
                

                上帝之手

                
                    <strong>7.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34865507/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="34865507">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2640615589.jpg" alt="小人物" data-x="2000" data-y="3000">
                
            </div>
            <p>
                

                小人物

                
                    <strong>7.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34927643/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34927643">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2702495844.jpg" alt="六号车厢" data-x="1400" data-y="2059">
                
            </div>
            <p>
                

                六号车厢

                
                    <strong>7.7</strong>
                
            </p>
        </a><a class="item" target="_blank" href="https://movie.douban.com/subject/34970325/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34970325">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2669238453.jpg" alt="无辜者" data-x="1382" data-y="2048">
                
            </div>
            <p>
                

                无辜者

                
                    <strong>7.1</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35240917/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35240917">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2696233262.jpg" alt="慕尼黑：战争边缘" data-x="2000" data-y="2963">
                
            </div>
            <p>
                

                慕尼黑：战争边缘

                
                    <strong>7.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/25828589/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="25828589">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2665872718.jpg" alt="黑寡妇" data-x="864" data-y="1280">
                
            </div>
            <p>
                

                黑寡妇

                
                    <strong>6.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30337388/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="30337388">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2677520025.jpg" alt="失控玩家" data-x="1080" data-y="1600">
                
            </div>
            <p>
                

                失控玩家

                
                    <strong>7.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26741632/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="26741632">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2637084112.jpg" alt="X特遣队：全员集结" data-x="2765" data-y="4096">
                
            </div>
            <p>
                

                X特遣队：全员集结

                
                    <strong>8.0</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34869121/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34869121">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2731403566.jpg" alt="警官之血" data-x="1200" data-y="1710">
                
            </div>
            <p>
                

                警官之血

                
                    <strong>6.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34841067/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="34841067">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2629056068.jpg" alt="你好，李焕英" data-x="3000" data-y="4292">
                
            </div>
            <p>
                

                你好，李焕英

                
                    <strong>7.7</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35262731/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35262731">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2675919720.jpg" alt="浅草小子" data-x="750" data-y="1111">
                
            </div>
            <p>
                

                浅草小子

                
                    <strong>8.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/32493124/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="32493124">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2641614433.jpg" alt="悬崖之上" data-x="5315" data-y="7440">
                
            </div>
            <p>
                

                悬崖之上

                
                    <strong>7.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/27124695/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="27124695">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2706359781.jpg" alt="智齿" data-x="1135" data-y="1585">
                
            </div>
            <p>
                

                智齿

                
                    <strong>7.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/33386178/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="33386178">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2722980045.jpg" alt="麦克白的悲剧" data-x="2025" data-y="3000">
                
            </div>
            <p>
                

                麦克白的悲剧

                
                    <strong>7.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26838236/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="26838236">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2685536675.jpg" alt="超能敢死队" data-x="1349" data-y="2000">
                
            </div>
            <p>
                

                超能敢死队

                
                    <strong>6.1</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/33457594/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="33457594">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2695961421.jpg" alt="摩加迪沙" data-x="1187" data-y="1701">
                
            </div>
            <p>
                

                摩加迪沙

                
                    <strong>8.1</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30344474/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30344474">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2807771124.jpg" alt="暗处的女儿" data-x="1120" data-y="1590">
                
            </div>
            <p>
                

                暗处的女儿

                
                    <strong>7.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34927916/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="34927916">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2687924214.jpg" alt="不速来客" data-x="2000" data-y="3006">
                
            </div>
            <p>
                

                不速来客

                
                    <strong>6.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30137576/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30137576">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2666266209.jpg" alt="记忆" data-x="629" data-y="900">
                
            </div>
            <p>
                

                记忆

                
                    <strong>7.7</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35205446/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35205446">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2684720964.jpg" alt="铁道英雄" data-x="4000" data-y="5600">
                
            </div>
            <p>
                

                铁道英雄

                
                    <strong>5.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/33437580/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="33437580">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2681332523.jpg" alt="天赐灵机" data-x="770" data-y="1100">
                
            </div>
            <p>
                

                天赐灵机

                
                    <strong>7.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35076714/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35076714">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2634360594.jpg" alt="扎克·施奈德版正义联盟" data-x="2025" data-y="3000">
                
            </div>
            <p>
                

                扎克·施奈德版正义联盟

                
                    <strong>8.1</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35123985/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35123985">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2678060278.jpg" alt="平行母亲" data-x="1434" data-y="2048">
                
            </div>
            <p>
                

                平行母亲

                
                    <strong>7.2</strong>
                
            </p>
        </a><a class="item" target="_blank" href="https://movie.douban.com/subject/34852249/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34852249">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2665017565.jpg" alt="杀出个黄昏" data-x="1455" data-y="2048">
                
            </div>
            <p>
                

                杀出个黄昏

                
                    <strong>6.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/33447864/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="33447864">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2766683184.jpg" alt="掘金" data-x="1124" data-y="1681">
                
            </div>
            <p>
                

                掘金

                
                    <strong>6.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30447440/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30447440">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2704450439.jpg" alt="Soho区惊魂夜" data-x="2126" data-y="3150">
                
            </div>
            <p>
                

                Soho区惊魂夜

                
                    <strong>6.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/33404512/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="33404512">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2627312853.jpg" alt="东京贵族女子" data-x="2891" data-y="4096">
                
            </div>
            <p>
                

                东京贵族女子

                
                    <strong>7.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35101435/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35101435">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2678164205.jpg" alt="斯宾塞" data-x="2001" data-y="2937">
                
            </div>
            <p>
                

                斯宾塞

                
                    <strong>6.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/33407124/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="33407124">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2641350668.jpg" alt="浪客剑心 最终章 追忆篇" data-x="1000" data-y="1416">
                
            </div>
            <p>
                

                浪客剑心 最终章 追忆篇

                
                    <strong>8.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30143331/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30143331">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2702918768.jpg" alt="红色通缉令" data-x="1500" data-y="2222">
                
            </div>
            <p>
                

                红色通缉令

                
                    <strong>6.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34966906/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34966906">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2706304062.jpg" alt="一个英雄" data-x="1944" data-y="2880">
                
            </div>
            <p>
                

                一个英雄

                
                    <strong>7.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30394797/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30394797">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2674321872.jpg" alt="尚气与十环传奇" data-x="1688" data-y="2500">
                
            </div>
            <p>
                

                尚气与十环传奇

                
                    <strong>6.1</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/27619748/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="27619748">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2622388983.jpg" alt="唐人街探案3" data-x="2143" data-y="3000">
                
            </div>
            <p>
                

                唐人街探案3

                
                    <strong>5.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/1428581/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="1428581">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2700138245.jpg" alt="天书奇谭" data-x="3481" data-y="4921">
                
            </div>
            <p>
                

                天书奇谭

                
                    <strong>9.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26140265/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="26140265">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2692391480.jpg" alt="新生化危机" data-x="1349" data-y="2000">
                
            </div>
            <p>
                

                新生化危机

                
                    <strong>4.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35030151/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35030151">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2682685788.jpg" alt="五个扑水的少年" data-x="2126" data-y="2976">
                
            </div>
            <p>
                

                五个扑水的少年

                
                    <strong>7.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/25909236/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="25909236">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2672792129.jpg" alt="致命感应" data-x="1200" data-y="1778">
                
            </div>
            <p>
                

                致命感应

                
                    <strong>6.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34963486/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34963486">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2635592713.jpg" alt="电影之神" data-x="707" data-y="1000">
                
            </div>
            <p>
                

                电影之神

                
                    <strong>7.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/25881778/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="25881778">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2641399262.jpg" alt="我要我们在一起" data-x="1080" data-y="1512">
                
            </div>
            <p>
                

                我要我们在一起

                
                    <strong>6.0</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34820925/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34820925">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2663190044.jpg" alt="钛" data-x="1938" data-y="2880">
                
            </div>
            <p>
                

                钛

                
                    <strong>6.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/3692602/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="3692602">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2710065784.jpg" alt="丛林奇航" data-x="4000" data-y="5922">
                
            </div>
            <p>
                

                丛林奇航

                
                    <strong>6.1</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34981939/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34981939">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2681328483.jpg" alt="偷窥者" data-x="1500" data-y="2222">
                
            </div>
            <p>
                

                偷窥者

                
                    <strong>6.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35158124/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35158124">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2673420377.jpg" alt="盛夏未来" data-x="1500" data-y="2175">
                
            </div>
            <p>
                

                盛夏未来

                
                    <strong>7.1</strong>
                
            </p>
        </a><a class="item" target="_blank" href="https://movie.douban.com/subject/34840705/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34840705">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2687136996.jpg" alt="呼朋引伴" data-x="4050" data-y="6000">
                
            </div>
            <p>
                

                呼朋引伴

                
                    <strong>7.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30465538/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30465538">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2655000580.jpg" alt="法兰西" data-x="2740" data-y="3732">
                
            </div>
            <p>
                

                法兰西

                
                    <strong>6.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35293160/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35293160">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2690943591.jpg" alt="在糟糕的日子里" data-x="1000" data-y="1423">
                
            </div>
            <p>
                

                在糟糕的日子里

                
                    <strong>7.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/27008393/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="27008393">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2719097587.jpg" alt="不老奇事" data-x="5906" data-y="8268">
                
            </div>
            <p>
                

                不老奇事

                
                    <strong>6.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35669441/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35669441">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2799276725.jpg" alt="希尔达与山丘之王" data-x="1360" data-y="2040">
                
            </div>
            <p>
                

                希尔达与山丘之王

                
                    <strong>8.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34881718/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34881718">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2707727239.jpg" alt="不可饶恕" data-x="1500" data-y="2222">
                
            </div>
            <p>
                

                不可饶恕

                
                    <strong>7.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35087699/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35087699">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2666591984.jpg" alt="中国医生" data-x="2126" data-y="2976">
                
            </div>
            <p>
                

                中国医生

                
                    <strong>6.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35299584/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35299584">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2680494037.jpg" alt="贝尔法斯特" data-x="1013" data-y="1500">
                
            </div>
            <p>
                

                贝尔法斯特

                
                    <strong>6.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30167974/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="30167974">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2627551613.jpg" alt="浪客剑心 最终章 人诛篇" data-x="2024" data-y="2866">
                
            </div>
            <p>
                

                浪客剑心 最终章 人诛篇

                
                    <strong>7.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30481476/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30481476">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2690707256.jpg" alt="国王理查德" data-x="1500" data-y="2223">
                
            </div>
            <p>
                

                国王理查德

                
                    <strong>7.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/10428501/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="10428501">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2629054917.jpg" alt="新·福音战士剧场版：终" data-x="1852" data-y="2621">
                
            </div>
            <p>
                

                新·福音战士剧场版：终

                
                    <strong>9.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34663377/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34663377">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2734449506.jpg" alt="路易斯·韦恩的激情人生" data-x="4051" data-y="6000">
                
            </div>
            <p>
                

                路易斯·韦恩的激情人生

                
                    <strong>7.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35196097/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35196097">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2684251260.jpg" alt="关于我妈的一切" data-x="1750" data-y="2500">
                
            </div>
            <p>
                

                关于我妈的一切

                
                    <strong>6.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35311473/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35311473">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2657020716.jpg" alt="孤狼之血2" data-x="750" data-y="1063">
                
            </div>
            <p>
                

                孤狼之血2

                
                    <strong>7.0</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30435124/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="30435124">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2655030796.jpg" alt="白蛇2：青蛇劫起" data-x="1879" data-y="3000">
                
            </div>
            <p>
                

                白蛇2：青蛇劫起

                
                    <strong>6.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35242942/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35242942">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2638021971.jpg" alt="倒霉性爱，发狂黄片" data-x="1313" data-y="1875">
                
            </div>
            <p>
                

                倒霉性爱，发狂黄片

                
                    <strong>7.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26935283/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="26935283">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2629260713.jpg" alt="侍神令" data-x="3571" data-y="4990">
                
            </div>
            <p>
                

                侍神令

                
                    <strong>5.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35287558/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35287558">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2642244414.jpg" alt="有答案的男子" data-x="1841" data-y="2560">
                
            </div>
            <p>
                

                有答案的男子

                
                    <strong>7.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35208823/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35208823">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2661923862.jpg" alt="灵媒" data-x="1500" data-y="2149">
                
            </div>
            <p>
                

                灵媒

                
                    <strong>6.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30279836/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="30279836">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2637603645.jpg" alt="第十一回" data-x="2000" data-y="2800">
                
            </div>
            <p>
                

                第十一回

                
                    <strong>7.2</strong>
                
            </p>
        </a><a class="item" target="_blank" href="https://movie.douban.com/subject/35465742/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35465742">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2681045224.jpg" alt="在你面前" data-x="1200" data-y="1710">
                
            </div>
            <p>
                

                在你面前

                
                    <strong>7.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30469922/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30469922">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2729074424.jpg" alt="密室逃生2" data-x="2000" data-y="2962">
                
            </div>
            <p>
                

                密室逃生2

                
                    <strong>6.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35017064/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35017064">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2652833060.jpg" alt="老去" data-x="3158" data-y="5000">
                
            </div>
            <p>
                

                老去

                
                    <strong>6.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35231370/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35231370">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2680735532.jpg" alt="峰爆" data-x="1000" data-y="1397">
                
            </div>
            <p>
                

                峰爆

                
                    <strong>6.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35280911/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35280911">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2633773335.jpg" alt="角色" data-x="2898" data-y="4096">
                
            </div>
            <p>
                

                角色

                
                    <strong>6.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30174085/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="30174085">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2673412189.jpg" alt="怒火·重案" data-x="1429" data-y="2000">
                
            </div>
            <p>
                

                怒火·重案

                
                    <strong>7.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34880302/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="34880302">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2632862664.jpg" alt="人潮汹涌" data-x="1429" data-y="2000">
                
            </div>
            <p>
                

                人潮汹涌

                
                    <strong>6.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26826330/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="26826330">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2628440875.jpg" alt="刺杀小说家" data-x="780" data-y="1196">
                
            </div>
            <p>
                

                刺杀小说家

                
                    <strong>6.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35691909/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="true" data-id="35691909">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2770879108.jpg" alt="鬼灭之刃 浅草篇" data-x="825" data-y="1180">
                
            </div>
            <p>
                
                    <span class="green">
                        <img src="https://img3.doubanio.com/f/movie/caa8f80abecee1fc6f9d31924cef8dd9a24c7227/pics/movie/ic_new.png" width="16" class="new">
                    </span>
                

                鬼灭之刃 浅草篇

                
                    <strong>8.7</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35477218/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35477218">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2670777611.jpg" alt="怪奇宅" data-x="1500" data-y="2138">
                
            </div>
            <p>
                

                怪奇宅

                
                    <strong>6.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26703121/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="26703121">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2653946775.jpg" alt="黑白魔女库伊拉" data-x="6759" data-y="10160">
                
            </div>
            <p>
                

                黑白魔女库伊拉

                
                    <strong>6.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35161768/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35161768">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2675958609.jpg" alt="夏日友晴天" data-x="1080" data-y="1542">
                
            </div>
            <p>
                

                夏日友晴天

                
                    <strong>7.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35547169/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35547169">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2699152497.jpg" alt="私人荒漠" data-x="1170" data-y="1716">
                
            </div>
            <p>
                

                私人荒漠

                
                    <strong>7.1</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/25728006/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="25728006">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2640611704.jpg" alt="速度与激情9" data-x="1080" data-y="1596">
                
            </div>
            <p>
                

                速度与激情9

                
                    <strong>5.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35158160/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35158160">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2630463690.jpg" alt="我的姐姐" data-x="5000" data-y="7478">
                
            </div>
            <p>
                

                我的姐姐

                
                    <strong>6.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35651911/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35651911">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2727626416.jpg" alt="鬼灭之刃 鼓屋敷篇" data-x="708" data-y="1000">
                
            </div>
            <p>
                

                鬼灭之刃 鼓屋敷篇

                
                    <strong>8.7</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34888057/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34888057">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2687662638.jpg" alt="甘草披萨" data-x="4320" data-y="6400">
                
            </div>
            <p>
                

                甘草披萨

                
                    <strong>7.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35251025/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35251025">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2690743436.jpg" alt="红色火箭" data-x="1382" data-y="2047">
                
            </div>
            <p>
                

                红色火箭

                
                    <strong>7.0</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35225859/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35225859">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2677331311.jpg" alt="小妈妈" data-x="1500" data-y="2222">
                
            </div>
            <p>
                

                小妈妈

                
                    <strong>7.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35259430/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35259430">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2675838753.jpg" alt="我们都无法成为大人" data-x="750" data-y="1059">
                
            </div>
            <p>
                

                我们都无法成为大人

                
                    <strong>7.5</strong>
                
            </p>
        </a><a class="item" target="_blank" href="https://movie.douban.com/subject/35198827/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35198827">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2656407373.jpg" alt="当男人恋爱时" data-x="1400" data-y="2100">
                
            </div>
            <p>
                

                当男人恋爱时

                
                    <strong>6.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30453797/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30453797">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2633279574.jpg" alt="浴火鸟" data-x="1000" data-y="1404">
                
            </div>
            <p>
                

                浴火鸟

                
                    <strong>7.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35573989/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35573989">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2678028129.jpg" alt="天空" data-x="1356" data-y="1929">
                
            </div>
            <p>
                

                天空

                
                    <strong>6.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34804147/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="34804147">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2628052135.jpg" alt="寻龙传说" data-x="2765" data-y="4096">
                
            </div>
            <p>
                

                寻龙传说

                
                    <strong>7.0</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/27605563/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="27605563">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2587966857.jpg" alt="鹿角" data-x="1334" data-y="2000">
                
            </div>
            <p>
                

                鹿角

                
                    <strong>5.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35202365/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35202365">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2685374824.jpg" alt="我是你的人" data-x="1131" data-y="1600">
                
            </div>
            <p>
                

                我是你的人

                
                    <strong>7.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35374186/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="true" data-id="35374186">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2652013893.jpg" alt="鸠的击退法" data-x="750" data-y="1059">
                
            </div>
            <p>
                
                    <span class="green">
                        <img src="https://img3.doubanio.com/f/movie/caa8f80abecee1fc6f9d31924cef8dd9a24c7227/pics/movie/ic_new.png" width="16" class="new">
                    </span>
                

                鸠的击退法

                
                    <strong>6.1</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35195869/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="true" data-id="35195869">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2854783787.jpg" alt="不良后果" data-x="2025" data-y="3000">
                
            </div>
            <p>
                
                    <span class="green">
                        <img src="https://img3.doubanio.com/f/movie/caa8f80abecee1fc6f9d31924cef8dd9a24c7227/pics/movie/ic_new.png" width="16" class="new">
                    </span>
                

                不良后果

                
                    <strong>6.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30378158/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="30378158">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2629408730.jpg" alt="秘密访客" data-x="6213" data-y="9047">
                
            </div>
            <p>
                

                秘密访客

                
                    <strong>5.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/33454993/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="33454993">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2638968571.jpg" alt="名侦探柯南：绯色的子弹" data-x="7785" data-y="10721">
                
            </div>
            <p>
                

                名侦探柯南：绯色的子弹

                
                    <strong>5.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/27594653/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="27594653">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2632091530.jpg" alt="发财日记" data-x="1656" data-y="2500">
                
            </div>
            <p>
                

                发财日记

                
                    <strong>5.7</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30176790/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30176790">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2706812406.jpg" alt="梅艳芳" data-x="1500" data-y="2140">
                
            </div>
            <p>
                

                梅艳芳

                
                    <strong>6.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/6874475/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="6874475">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2676934276.jpg" alt="混沌行走" data-x="2000" data-y="3012">
                
            </div>
            <p>
                

                混沌行走

                
                    <strong>5.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26856202/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="26856202">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2654489281.jpg" alt="安妮特" data-x="3484" data-y="4724">
                
            </div>
            <p>
                

                安妮特

                
                    <strong>6.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34779692/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="34779692">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2631711326.jpg" alt="新神榜：哪吒重生" data-x="4370" data-y="6201">
                
            </div>
            <p>
                

                新神榜：哪吒重生

                
                    <strong>6.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30229667/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30229667">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2637896820.jpg" alt="智能大反攻" data-x="1500" data-y="2222">
                
            </div>
            <p>
                

                智能大反攻

                
                    <strong>7.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/27200859/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="27200859">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2678455893.jpg" alt="来自远方" data-x="1780" data-y="2670">
                
            </div>
            <p>
                

                来自远方

                
                    <strong>9.1</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/33447881/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="33447881">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2666471566.jpg" alt="彼得罗夫的流感" data-x="2000" data-y="2941">
                
            </div>
            <p>
                

                彼得罗夫的流感

                
                    <strong>7.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30206311/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="30206311">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2651298629.jpg" alt="寂静之地2" data-x="3957" data-y="5793">
                
            </div>
            <p>
                

                寂静之地2

                
                    <strong>6.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/27077479/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="27077479">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2641811991.jpg" alt="招魂3" data-x="2764" data-y="4096">
                
            </div>
            <p>
                

                招魂3

                
                    <strong>6.4</strong>
                
            </p>
        </a><a class="item" target="_blank" href="https://movie.douban.com/subject/33450810/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="33450810">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2687175435.jpg" alt="羊崽" data-x="1170" data-y="1671">
                
            </div>
            <p>
                

                羊崽

                
                    <strong>5.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/29984000/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="29984000">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2654729576.jpg" alt="热带往事" data-x="1000" data-y="1414">
                
            </div>
            <p>
                

                热带往事

                
                    <strong>6.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35685660/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35685660">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2804529364.jpg" alt="2021去死" data-x="960" data-y="1350">
                
            </div>
            <p>
                

                2021去死

                
                    <strong>6.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35288767/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35288767">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2666303410.jpg" alt="革命者" data-x="2000" data-y="2789">
                
            </div>
            <p>
                

                革命者

                
                    <strong>7.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26604217/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="26604217">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2732133934.jpg" alt="里卡多一家" data-x="2700" data-y="4000">
                
            </div>
            <p>
                

                里卡多一家

                
                    <strong>6.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35151297/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35151297">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2669957808.jpg" alt="王国：北方的阿信" data-x="1200" data-y="1777">
                
            </div>
            <p>
                

                王国：北方的阿信

                
                    <strong>7.0</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35310153/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35310153">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2633604200.jpg" alt="较量2" data-x="579" data-y="873">
                
            </div>
            <p>
                

                较量2

                
                    <strong>7.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35287908/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35287908">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2672428635.jpg" alt="龙和雀斑公主" data-x="1446" data-y="2048">
                
            </div>
            <p>
                

                龙和雀斑公主

                
                    <strong>6.1</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34614665/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34614665">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2654990612.jpg" alt="静水城" data-x="1013" data-y="1500">
                
            </div>
            <p>
                

                静水城

                
                    <strong>7.1</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/27046740/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="27046740">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2642842673.jpg" alt="人之怒" data-x="2765" data-y="4096">
                
            </div>
            <p>
                

                人之怒

                
                    <strong>6.7</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30459571/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="30459571">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2678875868.jpg" alt="明日之战" data-x="1701" data-y="2721">
                
            </div>
            <p>
                

                明日之战

                
                    <strong>5.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/33973077/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="33973077">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2680748636.jpg" alt="皮皮鲁与鲁西西之罐头小人" data-x="3543" data-y="4961">
                
            </div>
            <p>
                

                皮皮鲁与鲁西西之罐头小人

                
                    <strong>6.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34908189/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="34908189">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2649579601.jpg" alt="老友记重聚特辑" data-x="2025" data-y="3000">
                
            </div>
            <p>
                

                老友记重聚特辑

                
                    <strong>9.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30351365/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30351365">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2681381987.jpg" alt="三层楼上" data-x="1417" data-y="1925">
                
            </div>
            <p>
                

                三层楼上

                
                    <strong>6.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34809114/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="34809114">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2588141278.jpg" alt="怪兽训练营" data-x="2025" data-y="3000">
                
            </div>
            <p>
                

                怪兽训练营

                
                    <strong>6.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/32568661/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="32568661">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2676932860.jpg" alt="妈妈的神奇小子" data-x="1819" data-y="2547">
                
            </div>
            <p>
                

                妈妈的神奇小子

                
                    <strong>6.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35236759/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35236759">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2669093839.jpg" alt="致胜女王" data-x="1939" data-y="2880">
                
            </div>
            <p>
                

                致胜女王

                
                    <strong>6.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35093796/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35093796">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2677276852.jpg" alt="奇迹" data-x="1979" data-y="2835">
                
            </div>
            <p>
                

                奇迹

                
                    <strong>7.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26613692/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="26613692">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2634253484.jpg" alt="哥斯拉大战金刚" data-x="2764" data-y="4096">
                
            </div>
            <p>
                

                哥斯拉大战金刚

                
                    <strong>6.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35210620/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35210620">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2672676397.jpg" alt="阿娜伊斯爱情" data-x="1200" data-y="1600">
                
            </div>
            <p>
                

                阿娜伊斯爱情

                
                    <strong>7.6</strong>
                
            </p>
        </a><a class="item" target="_blank" href="https://movie.douban.com/subject/35245762/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35245762">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2704531912.jpg" alt="神偷军团" data-x="1500" data-y="2222">
                
            </div>
            <p>
                

                神偷军团

                
                    <strong>6.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/27056396/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="27056396">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2651996671.jpg" alt="宝贝老板2" data-x="1293" data-y="2047">
                
            </div>
            <p>
                

                宝贝老板2

                
                    <strong>6.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/32493666/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="32493666">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2640758773.jpg" alt="追虎擒龙" data-x="4858" data-y="6802">
                
            </div>
            <p>
                

                追虎擒龙

                
                    <strong>5.0</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34973557/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34973557">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2641605963.jpg" alt="东京复仇者" data-x="2898" data-y="4096">
                
            </div>
            <p>
                

                东京复仇者

                
                    <strong>6.7</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30372022/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30372022">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2659155163.jpg" alt="绿衣骑士" data-x="1944" data-y="2880">
                
            </div>
            <p>
                

                绿衣骑士

                
                    <strong>6.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30213339/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="30213339">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2656009080.jpg" alt="比得兔2：逃跑计划" data-x="540" data-y="800">
                
            </div>
            <p>
                

                比得兔2：逃跑计划

                
                    <strong>7.0</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30216729/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30216729">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2647131304.jpg" alt="王牌保镖2" data-x="4320" data-y="6660">
                
            </div>
            <p>
                

                王牌保镖2

                
                    <strong>6.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35221424/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35221424">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2681647789.jpg" alt="之后3" data-x="809" data-y="1200">
                
            </div>
            <p>
                

                之后3

                
                    <strong>5.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/33450426/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="33450426">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2637809736.jpg" alt="电锯惊魂9：漩涡" data-x="1946" data-y="3000">
                
            </div>
            <p>
                

                电锯惊魂9：漩涡

                
                    <strong>5.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26820621/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="26820621">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2762894040.jpg" alt="西区故事" data-x="2063" data-y="3000">
                
            </div>
            <p>
                

                西区故事

                
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
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2665927388.jpg" alt="大红狗克里弗" data-x="961" data-y="1500">
                
            </div>
            <p>
                

                大红狗克里弗

                
                    <strong>6.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35184151/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35184151">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2626807774.jpg" alt="杀手寓言 第二章" data-x="2894" data-y="4096">
                
            </div>
            <p>
                

                杀手寓言 第二章

                
                    <strong>7.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30444940/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30444940">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2671039153.jpg" alt="恐惧街3" data-x="1500" data-y="2222">
                
            </div>
            <p>
                

                恐惧街3

                
                    <strong>7.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34857667/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34857667">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2668580982.jpg" alt="亚当斯一家2" data-x="1080" data-y="1600">
                
            </div>
            <p>
                

                亚当斯一家2

                
                    <strong>6.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35441797/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35441797">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2812277441.jpg" alt="新年快乐" data-x="1430" data-y="2048">
                
            </div>
            <p>
                

                新年快乐

                
                    <strong>6.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34856590/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34856590">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2670915379.jpg" alt="蓝色海湾" data-x="1046" data-y="1500">
                
            </div>
            <p>
                

                蓝色海湾

                
                    <strong>7.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30180126/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30180126">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2639263452.jpg" alt="窗里的女人" data-x="1500" data-y="2222">
                
            </div>
            <p>
                

                窗里的女人

                
                    <strong>6.1</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35283045/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35283045">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2734120983.jpg" alt="温柔酒吧" data-x="2000" data-y="3000">
                
            </div>
            <p>
                

                温柔酒吧

                
                    <strong>6.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26915921/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="26915921">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2675211748.jpg" alt="屏住呼吸2" data-x="2763" data-y="4096">
                
            </div>
            <p>
                

                屏住呼吸2

                
                    <strong>6.5</strong>
                
            </p>
        </a><a class="item" target="_blank" href="https://movie.douban.com/subject/30201133/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="30201133">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2654612159.jpg" alt="机动战士高达 闪光的哈萨维" data-x="1024" data-y="1445">
                
            </div>
            <p>
                

                机动战士高达 闪光的哈萨维

                
                    <strong>8.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34960130/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34960130">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2583403599.jpg" alt="深宅" data-x="720" data-y="960">
                
            </div>
            <p>
                

                深宅

                
                    <strong>5.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35360295/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35360295">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2652590749.jpg" alt="引见" data-x="1400" data-y="1995">
                
            </div>
            <p>
                

                引见

                
                    <strong>6.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35190036/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="true" data-id="35190036">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2678142009.jpg" alt="一切顺利" data-x="2740" data-y="3732">
                
            </div>
            <p>
                
                    <span class="green">
                        <img src="https://img3.doubanio.com/f/movie/caa8f80abecee1fc6f9d31924cef8dd9a24c7227/pics/movie/ic_new.png" width="16" class="new">
                    </span>
                

                一切顺利

                
                    <strong>7.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35259282/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35259282">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2687792757.jpg" alt="援助" data-x="1060" data-y="1500">
                
            </div>
            <p>
                

                援助

                
                    <strong>7.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26615748/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="26615748">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2654959196.jpg" alt="追忆迷局" data-x="729" data-y="1080">
                
            </div>
            <p>
                

                追忆迷局

                
                    <strong>6.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35204897/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35204897">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2636638694.jpg" alt="蜂蜜柠檬苏打" data-x="750" data-y="1056">
                
            </div>
            <p>
                

                蜂蜜柠檬苏打

                
                    <strong>5.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35375982/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35375982">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2685482998.jpg" alt="德维塔耶夫" data-x="1200" data-y="1800">
                
            </div>
            <p>
                

                德维塔耶夫

                
                    <strong>7.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/3439312/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="3439312">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2632043260.jpg" alt="猫和老鼠" data-x="4000" data-y="5823">
                
            </div>
            <p>
                

                猫和老鼠

                
                    <strong>5.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30389627/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30389627">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2662756946.jpg" alt="糖果人" data-x="2587" data-y="4096">
                
            </div>
            <p>
                

                糖果人

                
                    <strong>5.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35464967/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35464967">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2673396594.jpg" alt="硬汉枪神" data-x="960" data-y="1440">
                
            </div>
            <p>
                

                硬汉枪神

                
                    <strong>7.0</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35115642/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35115642">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2692942421.jpg" alt="平行森林" data-x="3508" data-y="4961">
                
            </div>
            <p>
                

                平行森林

                
                    <strong>6.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35116325/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35116325">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2691401250.jpg" alt="致命录像带94" data-x="1000" data-y="1500">
                
            </div>
            <p>
                

                致命录像带94

                
                    <strong>6.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/27177908/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="27177908">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2675197481.jpg" alt="凯特" data-x="1500" data-y="2222">
                
            </div>
            <p>
                

                凯特

                
                    <strong>6.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35271841/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35271841">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2742358006.jpg" alt="内特拉姆" data-x="1984" data-y="2835">
                
            </div>
            <p>
                

                内特拉姆

                
                    <strong>6.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35442458/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35442458">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2678672493.jpg" alt="老亨利" data-x="455" data-y="674">
                
            </div>
            <p>
                

                老亨利

                
                    <strong>7.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35164328/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35164328">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2634025511.jpg" alt="扫黑·决战" data-x="1435" data-y="2200">
                
            </div>
            <p>
                

                扫黑·决战

                
                    <strong>6.0</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30422485/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30422485">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2656934367.jpg" alt="人质" data-x="1187" data-y="1701">
                
            </div>
            <p>
                

                人质

                
                    <strong>6.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/3099221/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="3099221">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2643872011.jpg" alt="活死人军团" data-x="1500" data-y="2222">
                
            </div>
            <p>
                

                活死人军团

                
                    <strong>5.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26935358/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="26935358">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2709871678.jpg" alt="蜜熊的音乐奇旅" data-x="1080" data-y="1536">
                
            </div>
            <p>
                

                蜜熊的音乐奇旅

                
                    <strong>6.6</strong>
                
            </p>
        </a><a class="item" target="_blank" href="https://movie.douban.com/subject/35419225/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35419225">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2707359633.jpg" alt="风信子之恋" data-x="1070" data-y="1500">
                
            </div>
            <p>
                

                风信子之恋

                
                    <strong>7.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34873745/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34873745">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2676919475.jpg" alt="算牌人" data-x="2025" data-y="3000">
                
            </div>
            <p>
                

                算牌人

                
                    <strong>6.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26867808/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="26867808">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2685656324.jpg" alt="伯格曼岛" data-x="2766" data-y="4096">
                
            </div>
            <p>
                

                伯格曼岛

                
                    <strong>6.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35128768/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35128768">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2612400333.jpg" alt="希德尼娅的骑士 编织爱的行星" data-x="700" data-y="990">
                
            </div>
            <p>
                

                希德尼娅的骑士 编织爱的行星

                
                    <strong>8.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35516745/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35516745">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2674392637.jpg" alt="疯神" data-x="1276" data-y="1884">
                
            </div>
            <p>
                

                疯神

                
                    <strong>7.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/33440550/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="33440550">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2672784917.jpg" alt="塔米·菲的眼睛" data-x="1334" data-y="2000">
                
            </div>
            <p>
                

                塔米·菲的眼睛

                
                    <strong>6.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/27179288/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="27179288">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2665626425.jpg" alt="血色天劫" data-x="729" data-y="1080">
                
            </div>
            <p>
                

                血色天劫

                
                    <strong>6.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/1431694/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="1431694">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2693881679.jpg" alt="永不消逝的电波" data-x="2160" data-y="3030">
                
            </div>
            <p>
                

                永不消逝的电波

                
                    <strong>8.0</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34981336/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34981336">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2784021596.jpg" alt="新手" data-x="1000" data-y="1400">
                
            </div>
            <p>
                

                新手

                
                    <strong>7.1</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35384201/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35384201">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2681524736.jpg" alt="忠犬帕尔玛" data-x="1356" data-y="1929">
                
            </div>
            <p>
                

                忠犬帕尔玛

                
                    <strong>7.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34917447/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="34917447">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2658143548.jpg" alt="超越" data-x="1067" data-y="1600">
                
            </div>
            <p>
                

                超越

                
                    <strong>5.0</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35197314/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35197314">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2756608100.jpg" alt="警察局" data-x="810" data-y="1200">
                
            </div>
            <p>
                

                警察局

                
                    <strong>6.0</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35007363/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35007363">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2648204312.jpg" alt="命运/冠位指定 终局特异点 冠位时间神殿所罗门" data-x="2899" data-y="4096">
                
            </div>
            <p>
                

                命运/冠位指定 终局特异点 冠位时间神殿所罗门

                
                    <strong>6.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35429502/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35429502">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2647464257.jpg" alt="独自生活的人们" data-x="2000" data-y="2866">
                
            </div>
            <p>
                

                独自生活的人们

                
                    <strong>7.1</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34955909/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34955909">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2675863739.jpg" alt="猎魔人：狼之噩梦" data-x="1500" data-y="2222">
                
            </div>
            <p>
                

                猎魔人：狼之噩梦

                
                    <strong>7.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26823520/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="26823520">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2681329662.jpg" alt="日常幻想指南" data-x="4370" data-y="6201">
                
            </div>
            <p>
                

                日常幻想指南

                
                    <strong>4.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30400539/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30400539">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2680985686.jpg" alt="罪人" data-x="1500" data-y="2222">
                
            </div>
            <p>
                

                罪人

                
                    <strong>6.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30464901/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="30464901">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2641910067.jpg" alt="寻汉计" data-x="655" data-y="950">
                
            </div>
            <p>
                

                寻汉计

                
                    <strong>6.0</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26949852/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="26949852">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2625736779.jpg" alt="徐福" data-x="1300" data-y="1856">
                
            </div>
            <p>
                

                徐福

                
                    <strong>5.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30391228/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="30391228">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2654767767.jpg" alt="了不起的老爸" data-x="4370" data-y="6201">
                
            </div>
            <p>
                

                了不起的老爸

                
                    <strong>6.5</strong>
                
            </p>
        </a><a class="item" target="_blank" href="https://movie.douban.com/subject/34950968/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34950968">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2648204952.jpg" alt="少女☆歌剧 Revue Starlight 剧场版" data-x="566" data-y="800">
                
            </div>
            <p>
                

                少女☆歌剧 Revue Starlight 剧场版

                
                    <strong>8.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35178785/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35178785">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2692328438.jpg" alt="爱很难" data-x="1500" data-y="2222">
                
            </div>
            <p>
                

                爱很难

                
                    <strong>6.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35584688/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="true" data-id="35584688">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2851355051.jpg" alt="自拍复印机" data-x="750" data-y="1164">
                
            </div>
            <p>
                
                    <span class="green">
                        <img src="https://img3.doubanio.com/f/movie/caa8f80abecee1fc6f9d31924cef8dd9a24c7227/pics/movie/ic_new.png" width="16" class="new">
                    </span>
                

                自拍复印机

                
                    <strong>6.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30483429/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="true" data-id="30483429">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2834428418.jpg" alt="意学研究" data-x="1170" data-y="1718">
                
            </div>
            <p>
                
                    <span class="green">
                        <img src="https://img3.doubanio.com/f/movie/caa8f80abecee1fc6f9d31924cef8dd9a24c7227/pics/movie/ic_new.png" width="16" class="new">
                    </span>
                

                意学研究

                
                    <strong>5.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26818326/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="26818326">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2673991933.jpg" alt="西游记之再世妖王" data-x="1560" data-y="3000">
                
            </div>
            <p>
                

                西游记之再世妖王

                
                    <strong>5.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/33446375/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="33446375">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2675546699.jpg" alt="地陷" data-x="2000" data-y="2865">
                
            </div>
            <p>
                

                地陷

                
                    <strong>5.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35198690/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35198690">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2627012348.jpg" alt="剧场版 情色小说家~playback~" data-x="906" data-y="1280">
                
            </div>
            <p>
                

                剧场版 情色小说家~playback~

                
                    <strong>7.0</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35145064/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35145064">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2674501696.jpg" alt="谤法：在此矣" data-x="1700" data-y="2422">
                
            </div>
            <p>
                

                谤法：在此矣

                
                    <strong>6.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30037194/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30037194">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2629058776.jpg" alt="酷爱电影的庞波小姐" data-x="750" data-y="1065">
                
            </div>
            <p>
                

                酷爱电影的庞波小姐

                
                    <strong>7.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/25834936/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="25834936">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2657554193.jpg" alt="空中大灌篮：新传奇" data-x="2764" data-y="4096">
                
            </div>
            <p>
                

                空中大灌篮：新传奇

                
                    <strong>6.2</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34852311/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34852311">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2648436850.jpg" alt="酸酸甜甜" data-x="1383" data-y="2048">
                
            </div>
            <p>
                

                酸酸甜甜

                
                    <strong>6.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35115594/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35115594">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2632095592.jpg" alt="可能的任务" data-x="630" data-y="897">
                
            </div>
            <p>
                

                可能的任务

                
                    <strong>5.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35452679/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35452679">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2699933240.jpg" alt="童一个世界" data-x="4961" data-y="7016">
                
            </div>
            <p>
                

                童一个世界

                
                    <strong>7.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/10523152/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="10523152">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2675376450.jpg" alt="哭泣的男人" data-x="2160" data-y="3200">
                
            </div>
            <p>
                

                哭泣的男人

                
                    <strong>6.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35390972/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35390972">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2712253103.jpg" alt="粘在一起的隔离" data-x="1481" data-y="2222">
                
            </div>
            <p>
                

                粘在一起的隔离

                
                    <strong>7.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35183025/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35183025">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2722336852.jpg" alt="恋爱缺席的罗曼史" data-x="1187" data-y="1701">
                
            </div>
            <p>
                

                恋爱缺席的罗曼史

                
                    <strong>6.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35360566/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35360566">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2686465704.jpg" alt="当我们仰望天空时看见什么？" data-x="800" data-y="1185">
                
            </div>
            <p>
                

                当我们仰望天空时看见什么？

                
                    <strong>7.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/27089580/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="27089580">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2665617507.jpg" alt="恐惧街" data-x="1500" data-y="2222">
                
            </div>
            <p>
                

                恐惧街

                
                    <strong>5.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35009298/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35009298">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2660101405.jpg" alt="猪" data-x="1500" data-y="2222">
                
            </div>
            <p>
                

                猪

                
                    <strong>6.0</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35441896/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35441896">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2641806535.jpg" alt="命运理发师" data-x="581" data-y="909">
                
            </div>
            <p>
                

                命运理发师

                
                    <strong>7.6</strong>
                
            </p>
        </a><a class="item" target="_blank" href="https://movie.douban.com/subject/34945502/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34945502">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2623117831.jpg" alt="冠军" data-x="694" data-y="1000">
                
            </div>
            <p>
                

                冠军

                
                    <strong>7.5</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34881663/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34881663">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2661661947.jpg" alt="门徒" data-x="4050" data-y="6000">
                
            </div>
            <p>
                

                门徒

                
                    <strong>5.7</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34882845/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34882845">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2621616665.jpg" alt="世界起源" data-x="2740" data-y="3732">
                
            </div>
            <p>
                

                世界起源

                
                    <strong>5.7</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35522302/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35522302">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2673836120.jpg" alt="如获至宝" data-x="768" data-y="1024">
                
            </div>
            <p>
                

                如获至宝

                
                    <strong>7.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35150248/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35150248">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2723194489.jpg" alt="冤家宜解不宜结" data-x="1704" data-y="2360">
                
            </div>
            <p>
                

                冤家宜解不宜结

                
                    <strong>6.7</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34943349/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34943349">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2667391667.jpg" alt="疯女人的舞会" data-x="729" data-y="1080">
                
            </div>
            <p>
                

                疯女人的舞会

                
                    <strong>7.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30336307/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="30336307">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2656628179.jpg" alt="俑之城" data-x="2000" data-y="3000">
                
            </div>
            <p>
                

                俑之城

                
                    <strong>5.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/33433405/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="33433405">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2628845704.jpg" alt="大地" data-x="1013" data-y="1500">
                
            </div>
            <p>
                

                大地

                
                    <strong>7.4</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35122773/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35122773">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2628559841.jpg" alt="进入盛夏之门" data-x="1767" data-y="2500">
                
            </div>
            <p>
                

                进入盛夏之门

                
                    <strong>5.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35054837/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35054837">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2619484634.jpg" alt="新网球王子 冰帝 vs 立海 Game of Future" data-x="639" data-y="900">
                
            </div>
            <p>
                

                新网球王子 冰帝 vs 立海 Game of Future

                
                    <strong>6.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34839344/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="34839344">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2662473840.jpg" alt="完美受害人" data-x="3000" data-y="4257">
                
            </div>
            <p>
                

                完美受害人

                
                    <strong>4.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30465068/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30465068">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2632592932.jpg" alt="女生要革命" data-x="1500" data-y="2222">
                
            </div>
            <p>
                

                女生要革命

                
                    <strong>7.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35335784/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="35335784">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2631088441.jpg" alt="名侦探柯南：绯色的不在场证明" data-x="640" data-y="905">
                
            </div>
            <p>
                

                名侦探柯南：绯色的不在场证明

                
                    <strong>6.9</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34988584/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia_video">
        
            <div class="cover-wp" data-isnew="false" data-id="34988584">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2819529042.jpg" alt="千里不留行" data-x="770" data-y="1080">
                
            </div>
            <p>
                

                千里不留行

                
                    <strong>5.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/34954053/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="34954053">
                <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2628901958.jpg" alt="我没有谈的那场恋爱" data-x="1214" data-y="1734">
                
            </div>
            <p>
                

                我没有谈的那场恋爱

                
                    <strong>5.8</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35312401/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35312401">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2732882844.jpg" alt="月老" data-x="1433" data-y="2048">
                
            </div>
            <p>
                

                月老

                
                    <strong>7.0</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35463973/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35463973">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2664170473.jpg" alt="限制来电" data-x="2000" data-y="2866">
                
            </div>
            <p>
                

                限制来电

                
                    <strong>5.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/35182677/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="35182677">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2642827176.jpg" alt="犬部！" data-x="750" data-y="1059">
                
            </div>
            <p>
                

                犬部！

                
                    <strong>6.6</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/26996524/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="26996524">
                <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2627392971.jpg" alt="760号犯人" data-x="1944" data-y="2880">
                
            </div>
            <p>
                

                760号犯人

                
                    <strong>7.3</strong>
                
            </p>
        </a>
    
        
        <a class="item" target="_blank" href="https://movie.douban.com/subject/30444938/?tag=%E7%83%AD%E9%97%A8&amp;from=gaia">
        
            <div class="cover-wp" data-isnew="false" data-id="30444938">
                <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2668347584.jpg" alt="恐惧街2" data-x="1500" data-y="2222">
                
            </div>
            <p>
                

                恐惧街2

                
                    <strong>6.5</strong>
                
            </p>
        </a>"""
tree = etree.XML(xml)
result = tree.xpath("")