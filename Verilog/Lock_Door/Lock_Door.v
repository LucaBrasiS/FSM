`timescale 1ns / 1ps

module Lock_Door(
    input wire clk,
    input wire rst,
    input wire in,
    output reg unlocked,
    output reg [1:0] screen
);
    
    localparam s_idle = 4'b0001;
    localparam s_1    = 4'b0010;
    localparam s_2    = 4'b0100;
    localparam s_3    = 4'b1000;
    
    localparam sifre_giriniz       = 2'b00;
    localparam ilk_hane_hatali     = 2'b01;
    localparam ikinci_hane_hatali  = 2'b10;
    localparam hosgeldiniz         = 2'b11;
    
    localparam [2:0] TARGET_PASSWORD = 3'b101; // Hedef şifre: 101

    reg [3:0] cs, ns;
    reg [3:0] syc_in;
    reg [2:0] in_password;

    // 1. Adım: Durum Hafızası
    always @(posedge clk) begin
        if (rst) cs <= s_idle;
        else     cs <= ns;
    end
    
    // 2. Adım: Tuş Basma ve Sayaç Yönetimi
    always @(posedge clk) begin
        if (rst) begin
            in_password <= 3'b000;
            syc_in      <= 4'd0;
            screen      <= sifre_giriniz;
            unlocked    <= 1'b0;
        end else begin
            in_password[syc_in[1:0]] <= in;
            
            if (syc_in >= 2'd2) syc_in <= 4'd0;
            else                syc_in <= syc_in + 4'd1;
            
            case (cs)
                s_idle: begin
                    screen   <= sifre_giriniz;
                    unlocked <= 1'b0;
                end
                s_1: begin
                    if (in_password[0] != TARGET_PASSWORD[0])
                        screen <= ilk_hane_hatali;
                    else
                        screen <= sifre_giriniz;
                end
                s_2: begin
                    if (in_password[1] != TARGET_PASSWORD[1])
                        screen <= ikinci_hane_hatali;
                end
                s_3: begin
                    screen   <= hosgeldiniz;
                    unlocked <= 1'b1;
                end
                default: begin
                    screen   <= sifre_giriniz;
                    unlocked <= 1'b0;
                end
            endcase
        end
    end

    // 3. Adım: Sonraki Durum Mantığı (Combinational)
    always @(*) begin
        ns = cs;
        case (cs)
            s_idle: begin
                if (syc_in == 2'd1) begin
                    if (in_password[0] == TARGET_PASSWORD[0]) ns = s_1;
                    else                                      ns = s_idle;
                end
            end

            s_1: begin
                if (syc_in == 2'd2) begin
                    if (in_password[1] == TARGET_PASSWORD[1]) ns = s_2;
                    else                                      ns = s_idle;
                end
            end

            s_2: begin
                if (syc_in == 2'd0) begin
                    if (in_password[2] == TARGET_PASSWORD[2]) ns = s_3;
                    else                                      ns = s_idle;
                end
            end

            s_3: begin
                ns = s_idle;
            end

            default: ns = s_idle;
        endcase
    end

endmodule