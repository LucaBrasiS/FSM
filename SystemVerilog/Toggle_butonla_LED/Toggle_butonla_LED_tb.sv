`timescale 1ns / 1ps

module Toggle_butonla_LED_tb;

    logic clk;
    logic rst;
    logic led;

    // Test edilecek modülü (DUT) çağırıyoruz ve parametreyi 5 yapıyoruz ki hemen test edilsin
    Toggle_butonla_LED #(
        .HALF_PERIOD(5)
    ) uut (
        .clk(clk),
        .rst(rst),
        .led(led)
    );

    // Saat (Clock) Sinyali Üretimi (10ns periyot)
    always #5 clk = ~clk;

    initial begin
        // Başlangıç değerleri
        clk = 0;
        rst = 1;

        // 20ns sonra reset'i kaldır
        #20;
        rst = 0;

        // Sayacın sayıp LED'i toggle etmesini izlemek için yeterli süre verelim
        #150;
        $finish;
    end

    // Anlık takip
    initial begin
        $monitor("Zaman = %0t ns | rst = %b | Sayac (cnt) aktif | LED = %b", 
                 $time, rst, led);
    end

endmodule