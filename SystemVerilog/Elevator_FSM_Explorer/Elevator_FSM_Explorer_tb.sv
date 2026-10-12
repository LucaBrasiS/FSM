`timescale 1ns / 1ps

module elevator_controller_tb;

    // Sinyal tanımları
    logic       clk;
    logic       rst_n;
    logic [3:0] floor_req;
    logic       door_sensor;
    logic       emergency;
    
    logic [1:0] current_floor;
    logic       motor_up;
    logic       motor_down;
    logic       door_open;
    logic       alarm;
    logic [3:0] fsm_state;

    // Test edilecek modül (DUT)
    elevator_controller uut (
        .clk(clk),
        .rst_n(rst_n),
        .floor_req(floor_req),
        .door_sensor(door_sensor),
        .emergency(emergency),
        .current_floor(current_floor),
        .motor_up(motor_up),
        .motor_down(motor_down),
        .door_open(door_open),
        .alarm(alarm),
        .fsm_state(fsm_state)
    );

    // Saat Sinyali Üretimi (10ns periyot)
    always #5 clk = ~clk;

    initial begin
        // Başlangıç değerleri
        clk         = 0;
        rst_n       = 0;
        floor_req   = 4'b0000;
        door_sensor = 0;
        emergency   = 0;

        // 25ns sonra reset'i kaldır
        #25;
        rst_n = 1;

        // --- SENARYO 1: Kat 2'ye Git ---
        #20;
        floor_req = 4'b0100; // Kat 2 çağrısı (bit 2)
        #20;
        floor_req = 4'b0000; // Butonu bırak

        // Asansörün hedefe varıp kapı açmasını ve geri kapanmasını bekle
        #250;

        // --- SENARYO 2: Kapı Kapanırken Engel Sensörü (Obstacle) Testi ---
        floor_req = 4'b1000; // Kat 3 çağrısı
        #20;
        floor_req = 4'b0000;
        
        // Asansör Kat 3'e varıp kapı kapandığı sırada engel verelim
        #250;
        door_sensor = 1'b1; // Kapıda engel var!
        #30;
        door_sensor = 1'b0; // Engel çekildi

        #200;

        // --- SENARYO 3: Acil Durum (Emergency) Testi ---
        #50;
        emergency = 1'b1; // Acil stop basıldı
        #60;
        emergency = 1'b0; // Acil durum çözüldü

        #150;
        $finish;
    end

    // Anlık Durum Takibi ($monitor)
    initial begin
        $monitor("Zaman = %0t ns | State = %d | Kat = %d | Motor_Up = %b | Motor_Dn = %b | Door_Open = %b | Alarm = %b", 
                 $time, fsm_state, current_floor, motor_up, motor_down, door_open, alarm);
    end

endmodule