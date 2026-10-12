`timescale 1ns / 1ps

// ============================================================================
// ALL_TB: Beş FSM tasarımını tek simülasyonda test eden birleşik testbench
//   - Lock_Door            : doğru şifre (101), yanlış şifre (111), tekrar doğru
//   - Array2_Detector      : 1101 ve 1011 yakalama, hatalı dizi, örtüşen dizi
//   - FIFO                 : yazma/okuma sırası, dolu FIFO'ya yazma, boş FIFO'dan okuma
//   - elevator_controller  : kat çağrısı, kapıda engel, acil durum
//   - Toggle_butonla_LED   : HALF_PERIOD = 4 ile LED yanıp sönme
// Girişler saatin düşen kenarında değiştirilir; tasarımlar yükselen kenarda örnekler.
// ============================================================================
module ALL_TB;

    // ---------------- Ortak saat ve reset ----------------
    logic clk = 1'b0;
    logic rst;
    always #5 clk = ~clk;                  // 10 ns periyot (100 MHz)

    // ---------------- Lock_Door ----------------
    logic       lock_in;
    logic       unlocked;
    logic [1:0] screen;
    Lock_Door u_lock (.clk(clk), .rst(rst), .in(lock_in), .unlocked(unlocked), .screen(screen));

    // ---------------- Array2_Detector ----------------
    logic det_in;
    logic seq_a_detected, seq_b_detected;
    Array2_Detector u_det (.clk(clk), .rst(rst), .in(det_in),
                           .seq_a_detected(seq_a_detected), .seq_b_detected(seq_b_detected));

    // ---------------- FIFO ----------------
    logic       wr_en, rd_en;
    logic [7:0] din, dout;
    logic       empty, full;
    FIFO u_fifo (.clk(clk), .rst(rst), .wr_en(wr_en), .rd_en(rd_en), .din(din),
                 .dout(dout), .empty(empty), .full(full));

    // ---------------- elevator_controller ----------------
    logic [3:0] floor_req;
    logic       door_sensor, emergency;
    logic [1:0] current_floor;
    logic       motor_up, motor_down, door_open, alarm;
    logic [3:0] fsm_state;
    elevator_controller u_elev (.clk(clk), .rst_n(~rst), .floor_req(floor_req),
                                .door_sensor(door_sensor), .emergency(emergency),
                                .current_floor(current_floor), .motor_up(motor_up), .motor_down(motor_down),
                                .door_open(door_open), .alarm(alarm), .fsm_state(fsm_state));

    // ---------------- Toggle_butonla_LED ----------------
    logic led;
    Toggle_butonla_LED #(.HALF_PERIOD(4)) u_led (.clk(clk), .rst(rst), .led(led));

    // ---------------- Yardımcı görevler ----------------
    task automatic send_lock(input logic [2:0] bits);   // bits[0] ilk gönderilen hane
        for (int i = 0; i < 3; i++) begin
            lock_in = bits[i];
            @(negedge clk);
        end
    endtask

    task automatic send_det(input string s);           // "1101" gibi soldan sağa gönderir
        for (int i = 0; i < s.len(); i++) begin
            det_in = (s[i] == "1");
            @(negedge clk);
        end
    endtask

    task automatic fifo_write(input logic [7:0] d);
        wr_en = 1'b1; rd_en = 1'b0; din = d;
        @(negedge clk);
        wr_en = 1'b0;
    endtask

    task automatic fifo_read();
        wr_en = 1'b0; rd_en = 1'b1;
        @(negedge clk);
        rd_en = 1'b0;
    endtask

    task automatic call_floor(input int f);              // bir çevrimlik kat çağrısı
        floor_req = 4'b0001 << f;
        @(negedge clk);
        floor_req = 4'b0000;
    endtask

    // ---------------- Reset ----------------
    initial begin
        $timeformat(-9, 0, " ns", 7);
        rst = 1'b1;
        lock_in = 1'b0; det_in = 1'b0;
        wr_en = 1'b0; rd_en = 1'b0; din = 8'h00;
        floor_req = 4'b0000; door_sensor = 1'b0; emergency = 1'b0;
        repeat (2) @(negedge clk);
        rst = 1'b0;                                       // ilk aktif kenar: 25 ns
    end

    // ---------------- Lock_Door senaryosu ----------------
    initial begin
        wait (rst == 1'b0);
        send_lock(3'b101);   // BAŞARILI: 1-0-1 -> birkaç çevrim sonra unlocked = 1
        send_lock(3'b000);   // kilit açıldıktan sonraki çerçeve değerlendirilmez
        send_lock(3'b111);   // BAŞARISIZ: 2. hane yanlış -> S_IDLE
        send_lock(3'b101);   // BAŞARILI: tekrar açılır
        lock_in = 1'b0;
    end

    // ---------------- Array2_Detector senaryosu ----------------
    initial begin
        wait (rst == 1'b0);
        send_det("1101");    // BAŞARILI: seq_a_detected
        send_det("00");
        send_det("1011");    // BAŞARILI: seq_b_detected
        send_det("00");
        send_det("1100");    // BAŞARISIZ: algılama yok
        send_det("00");
        send_det("1101101"); // ÖRTÜŞME: A iki kez algılanır
        det_in = 1'b0;
    end

    // ---------------- FIFO senaryosu ----------------
    initial begin
        wait (rst == 1'b0);
        fifo_write(8'hAA); fifo_write(8'hBB); fifo_write(8'hCC);   // BAŞARILI: sırayla yaz
        fifo_read(); fifo_read(); fifo_read();                     // AA, BB, CC sırayla çıkar
        for (int i = 1; i <= 9; i++) fifo_write(8'h10 * i);        // BAŞARISIZ: 9. yazma (full) yok sayılır
        for (int i = 0; i < 9; i++)  fifo_read();                  // BAŞARISIZ: 9. okuma (empty) yok sayılır
    end

    // ---------------- Asansör senaryosu ----------------
    initial begin
        wait (rst == 1'b0);
        @(negedge clk);
        call_floor(2);                                   // BAŞARILI: Kat 2'ye git, kapı çevrimi
        wait (fsm_state == 4'b0110);                     // S_DOOR_CLOS
        wait (fsm_state == 4'b0000);                     // S_IDLE
        @(negedge clk);

        call_floor(0);                                   // Kat 0'a dön
        wait (fsm_state == 4'b0110);                     // kapı kapanırken...
        @(negedge clk) door_sensor = 1'b1;               // BAŞARISIZ: kapıda engel -> S_OBSTACLE
        repeat (3) @(negedge clk);
        door_sensor = 1'b0;
        wait (fsm_state == 4'b0000);
        @(negedge clk);

        call_floor(3);                                   // Kat 3'e giderken...
        wait (fsm_state == 4'b0001);                     // S_MOVING_UP
        repeat (2) @(negedge clk);
        emergency = 1'b1;                                // ACİL DURUM -> S_EMERGENCY
        repeat (4) @(negedge clk);
        emergency = 1'b0;                                // bırakılınca çağrıya devam eder
        wait (fsm_state == 4'b0110);                     // Kat 3'te kapı kapanıyor
        wait (fsm_state == 4'b0000);
        repeat (5) @(negedge clk);
        $display("Tum senaryolar tamamlandi: %t", $time);
        $finish;
    end

    // Güvenlik: simülasyon takılırsa durdur
    initial begin
        #5000;
        $display("Zaman asimi: %t", $time);
        $finish;
    end

    // ---------------- Konsol takibi ----------------
    always @(posedge clk) begin
        if (unlocked)       $display("%t | Lock_Door        : KILIT ACILDI", $time);
        if (seq_a_detected) $display("%t | Array2_Detector  : 1101 yakalandi", $time);
        if (seq_b_detected) $display("%t | Array2_Detector  : 1011 yakalandi", $time);
        if (alarm)          $display("%t | Elevator         : ACIL DURUM", $time);
    end

endmodule
